from librosa import load
from torch import argmax
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from jiwer import wer

processor = Wav2Vec2Processor.from_pretrained("chompk/wav2vec2-large-xlsr-thai-tokenized")
model = Wav2Vec2ForCTC.from_pretrained("chompk/wav2vec2-large-xlsr-thai-tokenized")

def process(file, target_text):
    audio, rate = load(file, sr = 16000)
    input_values = processor(audio, return_tensors="pt", sampling_rate=rate).input_values
    logits = model(input_values).logits
    prediction = argmax(logits, dim = -1)
    transcription = processor.batch_decode(prediction)[0]
    transcription = transcription.replace('[PAD]', '')
    transcription = transcription.replace(' ', '')
    # WORK WITH CER LATER
    metric = wer(hypothesis=transcription, truth=target_text)
    print(transcription)
    print(target_text)
    return metric
# venv\Scripts\activate.bat
# pip install transformers
# pip install librosa
# pip install torch
from librosa import load
from torch import argmax
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

audio, rate = load("TestAudio2.ogg", sr = 16000)
# print(audio, rate)

input_values = processor(audio, return_tensors="pt").input_values
logits = model(input_values).logits
prediction = argmax(logits, dim = -1)
transcription = processor.batch_decode(prediction)[0]
print(transcription)
from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained("tupleblog/salim-classifier")
model = AutoModelForSequenceClassification.from_pretrained("tupleblog/salim-classifier")
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


@app.get("/")
def predict(inputString: str):
    if len(inputString) < 50:
        inputString += "<pad>"
    return classifier(inputString)[0]["label"]

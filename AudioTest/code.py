# pip install datasets
from datasets.load import load_dataset


timit = load_dataset("timit_asr")
print(timit)
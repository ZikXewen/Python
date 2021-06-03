# venv\Scripts\activate.bat
# pip install transformers
# pip install librosa
# pip install torch
# pip install datasets
# pip install jiwer
from src import app

if __name__ == '__main__':
    app.run(debug = True)
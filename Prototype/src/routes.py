from flask import render_template, request, redirect, flash
from src.model import process
from src import app
@app.route('/')
def home_page():
    return render_template('home.html')
@app.route('/next', methods = ["GET", "POST"])
def next_page():
    if request.method == "POST":
        f = request.files["audio_data"]
        with open("audio.wav", "wb") as audio:
            f.save(audio)
        output = process("audio.wav", "สวัสดีครับพี่น้อง") #EXAMPLE TEXT
        print(output)
        return redirect('/next')
    else:
        return render_template('next.html')

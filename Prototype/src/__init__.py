from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = '2a6769226dfc04d56d3b6ce9'
from src import routes
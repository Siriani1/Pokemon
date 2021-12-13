from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask import send_file
import random, json

app = Flask(__name__)

CORS(app)


@app.route("/all")
def pokemon():
    return send_file('pokemon.json')


if __name__ == "__main__":
    app.run()
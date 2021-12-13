from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask import send_file
import random, json

app = Flask(__name__)

CORS(app)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/all")
def pokemon():
    return send_file('pokemon.json')

@app.route("/pikachu")
def pikachu():
    f = open('pokemon.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    return data['pokemon'][random.randrange(0,13)] #estrarre una riga a caso dal vettore data
    

@app.route("/charmender")
def charmender():
    f = open('pokemon.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    return data['pokemon'][random.randrange(0,13)] #estrarre una riga a caso dal vettore data


@app.route("/bulbasaur")
def bulbasaur():
    f = open('pokemon.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    return data['pokemon'][random.randrange(0,13)] #estrarre una riga a caso dal vettore data


@app.route("/snorlax")
def snorlax():
    f = open('pokemon.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    return data['pokemon'][random.randrange(0,13)] #estrarre una riga a caso dal vettore data






if __name__ == "__main__":
    app.run()
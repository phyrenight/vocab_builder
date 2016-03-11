from flask import Flask, flash, request, jsonify
import flask import session as login_session
from flask import make_response, url_for, redirect, render_template
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from vocab_db import Dict, Games, Base
from random import randint
app = Flask(__name__)

engine = create_engine('sqlite:///Dictionary.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def Home():
    return "Welcome home"

@app.route('/games')
def games():
	games = session.query(games).all()
    return render_template("games.html", games=games)

@app.route('/games/details/<gamesName>')
def gameDetails():
    return "Game details"


@app.route('/games/hangman/play')
def gameHangman():
    word = randomWord()
	hiddenWord = hideWord(word)
    return "hangman"

	
def randomWord():
    """
        randomly gets a word from the dictionary
		takes no parameters and returna 1 parameter
	"""
    max = session.query(Dict).count()
	number = randint(0, max)
    word = session.query(Dict).filter_by(id=number).one()
	return word


def hideWord(word):
    

if __name__ == '__main__'
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)


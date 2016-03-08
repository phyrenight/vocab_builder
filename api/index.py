from flask import Flask, flash, request, jsonify
import flask import session as login_session
from flask import make_response, url_for, redirect, render_template
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from vocab_db import Dict, Games, Base

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

@app.route('/games/hangman')
def gameHangman():
    return "hangman"

if __name__ == '__main__'
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)


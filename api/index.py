from flask import Flask, flash, request, jsonify
import flask import session as login_session
from flask import make_response, url_for, redirect, render_template
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from vocab_db import Dict, Base

app = Flask(__name__)

engine = create_engine('sqlite:///Dictionary.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def Home():
    retrun "Welcome home"

@app.route('/games')
def games():
    return "Welcome to the games page!"

if __name__ == '__main__'
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)


"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq
from functions import aq_data
from model import Record, DB

APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    aq_data.add_aq_to_db()
    DB.session.commit()
    return 'Data refreshed!'

@APP.route('/')
def root():
    """Base view."""
    # records = DB.query.filter(Record.value > 10).all()
    return str(aq_data.get_aq_data())
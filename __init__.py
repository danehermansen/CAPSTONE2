import os
from re import template 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import jinja2
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_person'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://danehermansen:goldsox2@localhost:5432/albumify'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = "supersecret"
app.jinja_env.undefined = jinja2.StrictUndefined
db.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))

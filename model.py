
from enum import auto
from sqlite3 import connect 
from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from __init__ import db, app

class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
    def get_id(self):
        return(self.user_id)  
class Albums(db.Model):

    __tablename__ = 'albums'

    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_name = db.Column(db.String(255), nullable=True)
    album_img = db.Column(db.String(255), nullable=True)
    album_runtime = db.Column(db.Float, nullable=True)

    def __init__(self, album_id, album_name, album_img, album_runtime):
        self.album_id = album_id
        self.album_name = album_name
        self.album_img = album_img
        self.album_runtime = album_runtime

class Reactions(db.Model):

    __tablemame__ = 'reactions'

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"), nullable=True)
    likes = db.Column(db.Boolean, primary_key=True)

    def __init__(self, likes):
        self.likes = likes


class Comments(db.Model):

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"), nullable=True)
    comment = db.Column(db.String)

    def __init__(self, comment_id, comment):
        self.comment_id = comment_id
        self.comment = comment
    

def connect_to_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://danehermansen:goldsox2@localhost:5432/albumify'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    app = Flask(__name__)
    connect_to_db(app)
    # db.drop_all()
    db.create_all()
    print("Connected to DB.")
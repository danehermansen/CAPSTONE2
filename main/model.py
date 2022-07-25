
from enum import auto
from sqlite3 import connect
# from turtle import back 
from flask import Flask
from flask_login import UserMixin, user_accessed
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from main import db

class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    comments = db.relationship('Comments', backref='users')
    user_albums = db.relationship('Albums', backref='users')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def get_id(self):
        return(self.user_id)  

class Albums(db.Model):

    __tablename__ = 'albums'

    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_name = db.Column(db.String(255), nullable=True) 
    user_id = db.Column(db.Integer,db.ForeignKey("users.user_id"))
    comments = db.relationship('Comments', backref='albums')

    def __init__(self, album_name):
        
        self.album_name = album_name
        
        

class Reactions(db.Model):

    __tablemame__ = 'reactions'

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id")) 
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"))
    likes = db.Column(db.Boolean, primary_key=True)
    

    def __init__(self, likes):
        self.likes = likes


class Comments(db.Model):

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"))
    
    comment = db.Column(db.String)

    def __init__(self, comment):
        
        self.comment = comment
        
    

# def connect_to_db(app):

#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://danehermansen:goldsox2@localhost:5432/albumify'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.app = app
#     db.init_app(app)

# if __name__ == "__main__":
#     app = Flask(__name__)
#     connect_to_db(app)
db.create_all()
#     print("Connected to DB.")
from json import load
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from curses import flash
import os
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
from main import app, login_manager
from main.model import  db, Users, Albums, Reactions, Comments
from flask_login import current_user, login_user, login_required, UserMixin
from main.newWheel import get_album



@login_manager.user_loader
# def load_user(user_id):
    
#     return Users.query.get(user_id)



def get_album_id(album_id):
    return Albums.query.get(album_id)

# def get_user_id(user_id):
#     if current_user.is_authenticated():
#         g.user = current_user.get_id()
#         return g.user

@app.route('/')
def homepage():
   

    return render_template('home.html')


@app.route('/login', methods=['POST','GET'])
def login_person():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for('user_profile'))

    return render_template('login.html', form=form)


@app.route('/sign_up', methods=['POST', 'GET'])
def user_sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        # user_id = Users(user_id=form.user_id.data).first()
        new_user = Users(username=form.username.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login_person'))
    return render_template('sign_up.html', form=form)

@app.route('/profile', methods=['POST', 'GET'])
# @login_required
def user_profile():
    # if current_user.is_authenticated():
    # user_id = current_user.get_id()
    # if form.validate_on_submit():
    #    get_album(form.album_name.data)
    #    new_album = Albums(album_name=form.album_name.data)
    #    db.session.add(new_album)
    #    db.session.commit()
    
    
    get_all_albums = Albums.query.all()
    form = FetchAlbum()
    comment_form = PersonComment()
    get_all_comments = Comments.query.all()
    if comment_form.validate_on_submit():
        new_comment = Comments(comment=comment_form.comment_user.data)
        db.session.add(new_comment)
        db.session.commit()
    elif form.validate_on_submit():
        get_album(form.album_name.data)
        new_album = Albums(album_name=form.album_name.data)
        db.session.add(new_album)
        db.session.commit()
        return redirect(url_for('user_profile'))

    
    
    

    
    return render_template('profile.html', form=form, comment_form=comment_form, albums=get_all_albums, comments=get_all_comments)



class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"}
    )
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"}
    )
    submit = SubmitField('Login')

   

class SignUpForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "username"}
    )
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "password"}
    )
    submit = SubmitField('Submit')

    def validate_username(self, username):
        existing_user_username = Users.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            flash('this username is already in use.')
            raise ValidationError("This username has been taken.")

    

class FetchAlbum(FlaskForm):
    album_name = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "album name"}
    )
    
    submit = SubmitField('Submit')


class PersonComment(FlaskForm):
    comment_user = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "comment"}
    )
    submit = SubmitField('Submit')

# class LikeButton():
#     l_user_id = Users.query.get(user_id).first()
#     load_user(l_user_id)
#     l_album_id = Albums.query.get(album_id).first()
#     get_album_id(l_album_id)
    

#     liked = Reactions(likes = True, album_id=l_album_id, user_id=l_user_id)
#     db.session.add(liked)
#     db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
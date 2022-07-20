from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from model import Users
from curses import flash
import os
from flask import Flask, render_template, request, session, flash, redirect, url_for
from __init__ import app, login_manager
from model import connect_to_db, db, Users, Albums, Reactions, Comments
from flask_login import login_user, login_required
@login_manager.user_loader
def load_user(user):
    return Users.query.get(int(user))

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
    return render_template('profile.html')


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"}
    )
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"}
    )
    submit = SubmitField('Login')

    # def validate_username(self, username):
    #     existing_user_username = Users.query.filter_by(
    #         username=username.data).first()
    #     # if existing_user_username:
    #     #     raise ValidationError("This username has been taken.")

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
        

if __name__ == "__main__":
    # connect_to_db(app)
    app.run(debug=True)
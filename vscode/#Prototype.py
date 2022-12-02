#Prototype
import flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#login
login_manager = LoginManager()
login_manager.init_app(app)

#user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default="default.jpg")
    messages = db.relationship('Message', backref='author', lazy=True)
    followers = db.Column(db.String(120), nullable=False, default="")

#messages table
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#home page
@app.route("/")
def home():
    return render_template('home.html')

#login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    return render_template('login.html')

#signup page
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

#logout
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

#view user home page
@app.route("/user/<username>")
@login_required
def user_home(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('home'))
    messages = Message.query.filter_by(user_id=user.id).all()
    return render_template('userhome.html', user=user, messages=messages)

#send public message
@app.route("/message", methods=['GET', 'POST'])
@login_required
def message():
    if request.method == 'POST':
        message_text = request.form['message']
        image_file = request.files['image']
        if image_file.filename != '':
            image_file.save(os.path.join('static/images', secure_filename(image_file.filename)))
            new_message = Message(message=message_text, image_file=image_file.filename, user_id=current_user.id)
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('user_home', username=current_user.username))
    return redirect(url_for('home'))

#send private message
@app.route("/private_message/<username>", methods=['GET', 'POST'])
@login_required
def private_message(username):
    user = User.query.filter_by(username=username).first()
    if request.method == 'POST':
        message_text = request.form['message']
        image_file = request.files['image']
        if image_file.filename != '':
            image_file.save(os.path.join('static/images', secure_filename(image_file.filename)))
            new_message = Message(message=message_text, image_file=image_file.filename, user_id=user.id)
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('user_home', username=username))
    return redirect(url_for('home'))

#view followers
@app.route("/followers/<username>")
@login_required
def followers(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('home'))
    followers = user.followers.split()
    return render_template('followers.html', user=user, followers=followers)

#edit profile
@app.route("/edit_profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.username = request.form['username']
        current_user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('user_home', username=current_user.username))
    return render_template('edit_profile.html', user=current_user)

#view profile
@app.route("/user/<username>/profile")
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('home'))
    return render_template('profile.html', user=user)

#follow user
@app.route("/follow/<username>")
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    follow_list = current_user.followers.split()
    if user.username not in follow_list:
        follow_list.append(user.username)
        current_user.followers = " ".join(follow_list)
        db.session.commit()
    return redirect(url_for('user_home', username=user.username))

#search for users
@app.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if user is None:
            return redirect(url_for('home'))
        return redirect(url_for('user_home', username=username))
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
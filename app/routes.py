from app import myapp_obj
from flask import render_template, redirect, flash, request, url_for
from app.forms import LoginForm
from app.models import User, Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, logout_user

@myapp_obj.route('/private')
@login_required
def private():
    return 'Hi this is a private page'

@myapp_obj.route('/logout')
@login_required
def logout():
    load_user(current_user)
    return redirect('/')

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        # search to make sure we have the user in our database
        user = User.query.filter_by(username=current_form.username.data).first()

        # check user's password with what is saved on the database
        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/login')

        # login user
        login_user(user, remember=current_form.remember_me.data)
        flash('quick way to debug')
        flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)
        return redirect('/')
    a = "Login Page"
    name = 'Returning User'
    return render_template('login.html', name=name, a=a, form=current_form)

@myapp_obj.route('/')
def home():
    return render_template('base.html')



@myapp_obj.route('/signup')
def signup():
    return render_template('signup.html')

@myapp_obj.route('/signup_handler', methods=['POST'])
def signup_handler():
    username = request.form['username']
    password = request.form['password']
    hashed_password = generate_password_hash(password)

    user = User(username=username, password=hashed_password)
    user.save()

    return redirect('/login')

#view user home page
@myapp_obj.route('/userhome')
#@login_required
def user_home(username):
    user = User.query.filter_by(username=username).first_or_404()
    messages = Message.query.filter_by(user_id=user.id).all()
    return render_template('user_home.html', user=user, messages=messages)

from app import myapp_obj, db
from flask import render_template, redirect, flash, request, url_for
from app.forms import LoginForm, SignupForm
from app.models import User, Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, logout_user

#login - isabel
@myapp_obj.route('/', methods=['POST', 'GET'])
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
            return redirect(url_for('home'))

        # login user
        login_user(user, remember=current_form.remember_me.data)
        #flash('quick way to debug')
        #flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)
        return redirect('/')
    titlePage = "Login Page"
    greetingMsg = 'Hello Returning User'
    return render_template('login.html', titlePage = titlePage, greetingMsg = greetingMsg, form=current_form)

#user profile - isabel
@myapp_obj.route('/user/<username>/profile')
@login_required
def profile():
    return render_template('profile.html')

#view followers - isabel
@myapp_obj.route('/user/<username>/followers')
@login_required
def followers():

    return render_template('followers.html')

#private message - isabel
@myapp_obj.route('/user/<username>/message')
@login_required
def message():
    return render_template('message.html')

#logout
#@myapp_obj.route('/logout')
#@login_required
#def logout():
#    #load_user(current_user)
#    logout_user(current_user)
#    return redirect('/')

@myapp_obj.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have logged out')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

#create an account
@myapp_obj.route('/signup', methods = ['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))           #if user is logged in, go to homepage
    current_form = SignupForm()

    #On submission, checks if data is accepted by all field validators
    if current_form.validate_on_submit():
        user = User(username=current_form.username.data)
        user.set_password(current_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account creation successful!')
        return redirect(url_for('login'))
    return render_template('signup.html', form=current_form)

#
@myapp_obj.route('/signup_handler', methods=['POST'])
def signup_handler():
    username = request.form['username']
    password = request.form['password']
    hashed_password = generate_password_hash(password)

    user = User(username=username, password=hashed_password)
    user.save()

    return redirect('/login')

#view user home page
#@myapp_obj.route('/homepage')
#@login_required
#def home(username):
#    user = User.query.filter_by(username=username).first_or_404()
#    messages = Message.query.filter_by(user_id=user.id).all()
#   return render_template('user_home.html', user=user, messages=messages)


@myapp_obj.route('/home')
@login_required
def home():
    current_user.username = User.query.filter_by(username=current_user.username).first()
    message = Message.query.filter_by(user_id=current_user.username.id).all()
    return render_template('user_home.html', titlePage = titlePage, message = message)



#delete account
@myapp_obj.route('/delete_account', methods=['POST'])
def delete_account():
    user_id = request.form['user_id']
    user_to_delete = User.query.filter_by(id=user_id).first()

    if user_to_delete is not None:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash('Account deleted successfully')

    return redirect('/home')

#view profile
@myapp_obj.route('/user/<username>/profile', methods=['POST', 'GET'])
@login_required
def view_profile():

    user = User.query.filter_by(username=username).first()

    if user is None:
        flash('User not found.')
        return redirect(url_for('home'))

    return render_template('profile.html', user=user)
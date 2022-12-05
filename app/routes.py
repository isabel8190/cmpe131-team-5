from app import myapp_obj, db
from flask import render_template, redirect, flash, request, url_for
from app.forms import LoginForm, SignupForm, PostForm, EditProfileForm
from app.models import User, Message#, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, logout_user

#login - isabel
@myapp_obj.route('/', methods=['POST', 'GET'])
def login():
    #if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home', username = current_user.username))

    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        # search to make sure we have the user in our database
        user = User.query.filter_by(username=current_form.username.data).first()

        # check user's password with what is saved on the database
        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect(url_for('login'))

        # login user
        login_user(user, remember=current_form.remember_me.data)
        #flash('quick way to debug')
        #flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)

        #if login is successful, go to home page with username in url
        return redirect(url_for('home', username = current_form.username.data))
    return render_template('login.html', form=current_form)

#logout - sherif
@myapp_obj.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have logged out')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

#user profile - isabel
@myapp_obj.route('/user/<username>/profile/')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()

    #FILl THIS OUT

    return render_template('profile.html', user=user)

#edit profile - isabel
@myapp_obj.route('/user/<username>/profile/edit', methods=['POST', 'GET'])
@login_required
def edit(username):
    user = User.query.filter_by(username=username).first_or_404()
    current_form = EditProfileForm()

    if current_form.validate_on_submit():
        # check user's password with what is saved on the database
        if not user.check_password(current_form.confirmPassword.data):
            flash('Incorrect password, changes not saved.')
            # if passwords don't match, send user to edit again
            return redirect(url_for('edit', username=username))

        #current_user.picture = current_form.picture.data

        if len(current_form.newUsername.data) != 0:
            user.set_username(current_form.newUsername.data) 
            flash('Password changed!')
            db.session.commit()
        if len(current_form.newPassword.data) != 0:
            user.set_password(current_form.newPassword.data)
            flash('Username changed!')
            db.session.commit()
        flash('Please keep your login information in a safe place!')
        return redirect(url_for('login'))

    return render_template('edit.html' ,user=user, form=current_form)

#view followers - isabel
@myapp_obj.route('/user/<username>/followers')
@login_required
def followers(username):
    
    return render_template('followers.html')

#view following - isabel
@myapp_obj.route('/user/<username>/following')
@login_required
def following(username):
    
    return render_template('following.html')

#private message - isabel
@myapp_obj.route('/user/<username>/message')
@login_required
def message(username):
    return render_template('message.html')

#create an account - isabel
@myapp_obj.route('/signup', methods = ['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home', username = current_user.username))           #if user is logged in, go to homepage
    current_form = SignupForm()

    #On submission, checks if data is acccepted by all field validators
    if current_form.validate_on_submit():
        user = User(username=current_form.username.data)
        user.set_password(current_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account creation successful!')
        return redirect(url_for('login'))
    return render_template('signup.html', form=current_form)

#view user home page
@myapp_obj.route('/user/<username>/home', methods = ['POST', 'GET'])
@login_required
def home(username):
    current_form = PostForm()
    user = User.query.filter_by(username=username).first_or_404()
    #messages = Message.query.filter_by(user_id=user.id).all()
    return render_template('home.html', user=user, form = current_form) #, messages=messages)

'''
@myapp_obj.route('/userhome')
@login_required
def home():
    current_user.username = User.query.filter_by(username=current_user.username).first()
    message = Message.query.filter_by(user_id=current_user.username.id).all()
    return render_template('user_home.html', titlePage = titlePage, message = message)
'''

#delete account:
@myapp_obj.route('/user/delete', methods=['POST'])
@login_required
def delete():
    user_id = request.form['user_id']
    user_to_delete = User.query.filter_by(id=user_id).first()

    if user_to_delete is not None:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash('Account deleted successfully') 

    return redirect('/')

'''
@myapp_obj.route('/user/<username>/profile/edit', methods=['POST', 'GET'])
@login_required
def edit_profile(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        flash('User not found.')
        return redirect(url_for('home'))

    return render_template('edit.html', user=user)
'''

#Edit profile
@myapp_obj.route('/user/<username>/edit_profile_handler', methods=['POST'])
@login_required
def edit_profile_handler():
    user_id = request.form['user_id']
    display_name = request.form['display_name']
    about_me = request.form['about_me']

    user = User.query.filter_by(id=user_id).first()

    if user is None:
        flash('User not found.')
        return redirect(url_for('home'))

    user.display_name = display_name
    user.about_me = about_me
    db.session.commit()

    return redirect('/user/' + user.username + '/profile')

#follow or unfollow a user
@myapp_obj.route('/user/<username>/follow', methods=['POST'])
@login_required
def follow_handler():
    user_id = request.form['user_id']
    user_to_follow = User.query.filter_by(id=user_id).first()

    if user_to_follow is None:
        flash('User not found.')
        return redirect(url_for('home'))

    if user_to_follow in current_user.following:
        current_user.following.remove(user_to_follow)
        flash('You stopped following ' + user_to_follow.username + '.')
    else:
        current_user.following.append(user_to_follow)
        flash('You are now following ' + user_to_follow.username + '.')

    db.session.commit()
    return redirect('/user/' + user_to_follow.username + '/profile')


    
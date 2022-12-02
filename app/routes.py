from app import myapp_obj
from flask import render_template, redirect, flash, url_for, request
from app.forms import LoginForm
from app.models import User, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename #
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

#send private message
@myapp_obj.route("/private_message/<username>", methods=['GET', 'POST'])
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
@myapp_obj.route("/followers/<username>")
@login_required
def followers(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('home'))
    followers = user.followers.split()
    return render_template('followers.html', user=user, followers=followers)

@myapp_obj.route('/')
def home():
    return render_template('home.html')

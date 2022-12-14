from app import myapp_obj, db
from flask import render_template, redirect, flash, request, url_for
from app.forms import LoginForm, SignupForm, PostForm, EditProfileForm, SearchForm
from app.models import User #, Message #, Post
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
        user.set_bio("")
        db.session.add(user)
        db.session.commit()
        flash('Account creation successful!')
        return redirect(url_for('login'))
    return render_template('signup.html', form=current_form)

#logout - sherif
@myapp_obj.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have logged out')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

#delete confirmation - isabel
@myapp_obj.route('/user/<username>/deleteConfirm', methods=['POST', 'GET'])
@login_required
def deleteConfirm(username):
    user = User.query.filter_by(username=username).first()
    return render_template('delete.html', user=user)

#delete account - isabel
@myapp_obj.route('/user/<username>/delete', methods=['POST', 'GET'])
@login_required
def delete(username):
    user = User.query.filter_by(username=username).first_or_404()
    db.session.delete(user)
    db.session.commit()
    flash('Account deleted successfully')
    return redirect(url_for('login'))    #redirect to login

#user profile - isabel
@myapp_obj.route('/user/<username>/profile/')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user)

#edit profile - isabel
@myapp_obj.route('/user/<username>/profile/edit', methods=['POST', 'GET'])
@login_required
def edit(username):
    user = User.query.filter_by(username=username).first()
    current_form = EditProfileForm()
    if current_form.validate_on_submit():
        # check user's password with what is saved on the database
        if not user.check_password(current_form.confirmPassword.data):
            flash('Incorrect password, changes not saved.')
            # if passwords don't match, send user to edit again
            return redirect(url_for('edit', username=username))

        #current_user.picture = current_form.picture.data

        if len(current_form.newPassword.data) != 0:
            user.set_password(current_form.newPassword.data)
            flash('Password changed!')
            db.session.commit()
        if len(current_form.newBio.data) != 0:
            user.set_bio(current_form.newBio.data) 
            flash('Bio changed!')
            db.session.commit()
        if len(current_form.newUsername.data) != 0:
            name = User.query.filter_by(username=current_form.newUsername.data).first()
            print(name)
            if name is not None:
                flash('Choose another username')
                return redirect(url_for('edit', username=username))
            user.set_username(current_form.newUsername.data) 
            flash('Username changed!')
            db.session.commit()
        return redirect(url_for('login'))

    return render_template('edit.html' ,user=user, form=current_form)

#view followers - isabel
@myapp_obj.route('/user/<username>/followers')
@login_required
def followers(username):
    user = User.query.filter_by(username=username).first()
    num = 0
    for followers in user.followers:
        num += 1
    return render_template('followers.html', user=user, num = num)

#view following - isabel
@myapp_obj.route('/user/<username>/following')
@login_required
def following(username):
    user = User.query.filter_by(username=username).first()
    num = 0
    for following in user.followed:
        num += 1

    return render_template('following.html', user=user, num = num)

#search user - isabel
@myapp_obj.route('/user/<username>/search', methods=['POST', 'GET'])
@login_required
def search(username):
    current_form = SearchForm()

    #On submission, checks if data is acccepted by all field validators
    if current_form.validate_on_submit():
        if(current_form.search.data == current_user.username):
            flash("You cannot search for yourself!")
            return redirect(url_for('search', username = current_user.username))

        user = User.query.filter_by(username=current_form.search.data).first()
        return render_template(('searchResults.html'), form = current_form, username = user.username)

    return render_template('search.html', user=username, form= current_form)

#search profile - isabel
@myapp_obj.route('/user/searchProfile/<username>', methods=['POST', 'GET'])
@login_required
def searchProfile(username):
    user = User.query.filter_by(username=username).first()
    return render_template('searchProfile.html', username=user)

#private message - bhargavi
@myapp_obj.route('/user/<username>/message')
@login_required
def message(username):
    return render_template('message.html', user=username)
'''
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    current_form = MessageForm()
    if current_form.validate_on_submit():
        msg = Message(author=current_user, recipient=user, body=form.message.data)
        db.session.add(msg)
        db.session.commit()
        flash(_('Your message has been sent.'))
        return redirect(url_for('/user/<username>/message'))
    return render_template('send_message.html', title=_('Send Message'),
                           form=form, recipient=recipient)
'''

#follow - isabel
@myapp_obj.route('/user/searchProfile/<username>/follow', methods=['POST', 'GET'])
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    #user does not exist, here bc some people might edit links
    if user is None:
        flash("User does not exist")
        return redirect(url_for('search', username = current_user.username))
    else:
        current_user.follow(user)
        db.session.commit()
        return redirect(url_for('searchProfile',username = username))

#unfollow - isabel
@myapp_obj.route('/user/searchProfile/<username>/unfollow', methods=['POST', 'GET'])
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()

    #user does not exist, here bc some people might edit links
    if user is None:
        flash("User does not exist")
        return redirect(url_for('search', username = current_user.username))
    else:
        current_user.unfollow(user)
        db.session.commit()
        return redirect(url_for('searchProfile',username = username))

#view user home page
@myapp_obj.route('/user/<username>/home', methods = ['POST', 'GET'])
@login_required
def home(username):
    current_form = PostForm()
    user = User.query.filter_by(username=username).first_or_404()
    #messages = Message.query.filter_by(user_id=user.id).all()
    return render_template('home.html', user=user, form = current_form) #, messages=messages)

'''
#upload images - bhargavi
@app.route('/user/<username>/home', methods=['GET', 'POST']) #maybe switch home with a new tab (like /images or /uploads) if it doesn't work?
@login_required
def upload_image():
    if request.method == "POST":
        if file.filename == '':
            flash('No file was selected')
        if request.files:
            image = request.files["image"]
            flash('Image successfully Uploaded')
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            filename = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
            print("stored as:" + filename)
            return render_template("upload_image.html", uploaded_image=filename)
    return render_template("upload_image.html") #if no image is selected it's redirect back to the same page
'''

'''
#upload images - bhargavi
@app.route('/user/<username>/home', methods=['GET', 'POST']) #maybe switch home with a new tab (like /images or /uploads) if it doesn't work?
@login_required
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
    	flash('No file was selected')
    else
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('home.html'))
    
  #note: might need to add an "upload image" button to home for this one?
'''


'''
@myapp_obj.route('/userhome')
@login_required
def home():
    current_user.username = User.query.filter_by(username=current_user.username).first()
    message = Message.query.filter_by(user_id=current_user.username.id).all()
    return render_template('user_home.html', titlePage = titlePage, message = message)
'''

#Python function to check browser type - sherif
@myapp_obj.route('/check_browser', methods=['POST', 'GET'])
@login_required
def check_browser():
    # To get the browser type
    browser = request.headers.get('User-Agent')
    if 'Chrome' in browser:
        flash('Google Chrome is compatible with this website.')
    else:
        flash('It is recommended to use Google Chrome for this website.')
    return redirect(url_for('home', username = current_user.username))

    

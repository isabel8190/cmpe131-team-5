#python code

#Functional Requirements


#Login 
#Logout 
#Create a new account 
#Delete account
#View user home page (user can see messages of users they follow) 
#Send public messages to followers (may include images)
#Send/receive private messages
#View followers 
#Edit the user's profile. 
#View a user profile.
#Follow other users.
#Search for other users. 


#Python Code 

#Login
def login(username, password):
    if check_credentials(username, password):
        return True
    else:
        return False

#Logout
def logout(username):
    if logout_user(username):
        return True
    else:
        return False

#Create a new account 
def create_account(username, password):
    if create_user_account(username, password):
        return True
    else:
        return False

#Delete Account
def delete_account(username):
    if delete_user_account(username):
        return True
    else:
        return False

#View user home page
def view_home_page(username):
    user_info = get_user_info(username)
    followers = get_followers(username)
    messages = get_messages_by_followers(followers)
    return user_info, followers, messages

#Send public messages 
def send_public_message(username, message):
    if post_message(username, message):
        return True
    else:
        return False

#Send/receive private messages
def send_private_message(username, message, recipient):
    if send_message(username, message, recipient):
        return True
    else:
        return False

def receive_private_message(username):
    messages = get_messages(username)
    return messages

#View followers 
def view_followers(username):
    followers = get_followers(username)
    return followers

#Edit the user's profile.
def edit_profile(username, new_data):
    if update_user_data(username, new_data):
        return True
    else:
        return False

#View a user profile.
def view_profile(username):
    user_data = get_user_data(username)
    return user_data

#Follow other users.
def follow_user(username, user_to_follow):
    if follow(username, user_to_follow):
        return True
    else:
        return False

#Search for other users.
def search_users(username):
    users = search_user(username)
    return users

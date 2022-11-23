## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login (Isabel)
2. Logout (Isabel)
3. Create a new account (Bhargavi)
4. Delete account (Bhargavi)
5. View user home page (user can see messages of users they follow) (Bhargavi)
6. Send public messages to followers (may include images) (Bhargavi)
7. View private messages from their followers.
8. Send private message to followers.
9. Edit user's profile.
10. View a user profile. (Isabel)
11. Follow other users. (Isabel)
12. Search for other users.

## Non-functional Requirements

1. The system login must be secure (entering the wrong password/username means the user is denied access).
2. The system must be available 24/7.
3. The system is expected to work on Mac/Windows/Linux.
4. The system is expected to work on Google Chrome.

## Use Cases

1. Follow other users (Isabel)
- **Pre-condition:**
1. User must be signed in.

- **Trigger:**
User clicked on "Follow" button.

- **Primary Sequence:**
  
  1. User searches for another user's username (ex: @user2).
  2. System redirects user to the other user's profile picture. (ex: go to user2's profile)
  3. User clicks the "Follow" button.
  4. System adds the other user to list of user's following list. (ex: adds user2 into user's following list)
  5. System refreshes the page and changes the "Follow" button to "Following".

- **Primary Postconditions:**
The user is following another user and can see the followed user's content on the home page.

2. View user's profile (Isabel)
- **Pre-condition:** 
1. User is logged into their account.

- **Trigger:** 
User clicks on a username or the "My Profile" button.

- **Primary Sequence:**
  
  1. User clicks on another user's username.
  2. System redirects user to the profile page corresponding to the username.

- **Primary Postconditions:** 
The user is on a profile page.

- **Alternate Sequence:** 
  
  1. User clicks on the "My Profile" button.
  2. System redirects the user to their profile page.

3. Create New account (Bhargavi)
- **Pre-condition:** 
  1. User must have a valid email address
  2. User does not have an existing account
  3. Username or email is unique and different from existing username

- **Trigger:** 
  User Clicks "Create Account" button

- **Primary Sequence:**
  
  1. User enters their email address and a password
  2. User clicks “create account” button
  3. System redirects user to their new profile.

- **Primary Postconditions:**
  User is on their new profile page

- **Alternate Sequence:** 
  1. User clicks on “create account” button.
  2. System says their email is invalid
  3. User enters a correct email address
  4. System redirects user to their homepage

- **Alternate Sequence:** 
  1. User clicks on “create account” button.
  2. System says their username/email is taken
  3. User enters a different username/email
  4. System redirects user to their homepage

4. Send Public Messages (Bhargavi)
- **Pre-condition:**
  1. User is logged into their account.
  2. User is on their homepage

- **Trigger:** 
  User clicks the "Post" button

- **Primary Sequence:**
  
  1. User enters their message into a text box.
  2. User enters an image if they want to include one.
  3. User clicks the “Post” button in order to send the message.


- **Primary Postconditions:** 
  The user’s message is posted and can be seen by others.

- **Alternate Sequence:** 
  1. User is looking at their profile
  2. User goes to their homepage.
  3. System redirects the user to their profile page
  4. User Enters their message and clicks “post”


5. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

6. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

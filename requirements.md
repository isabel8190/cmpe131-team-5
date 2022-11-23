## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login (Isabel)
2. Logout (Isabel)
3. Create a new account (Bhargavi)
4. Delete account (Bhargavi)
5. View user home page (user can see messages of users they follow) (Bhargavi)
6. Send public messages to followers (may include images) (Bhargavi)
7. View private messages from their followers.(Sherif)
8. Send private message to followers.(Sherif)
9. Edit user's profile.(Sherif)
10. View a user profile. (Isabel)
11. Follow other users. (Isabel)
12. Search for other users.(Sherif)

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

3. View User Home page (Bhargavi)
- **Pre-condition:** 
  1. User must be logged in

- **Trigger:** 
  User Clicks on "home page" button

- **Primary Sequence:**
  
  1. User clicks on the "home page" button
  2. System redirects user to their homepage.

- **Primary Postconditions:**
  User is on their home page

- **Alternate Sequence:** 
  1. User clicks on profile
  2. From profile user clicks the "Home page" button
  3. System redirects user to their homepage.

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


5. view private message (Sherif) 
- **Pre-condition:** 
  1. The user must be logged in 
  2. The user must be on their home screen 


- **Trigger:** 
  User clicks on a specific message

- **Primary Sequence:**
  
  1. The user clicks on the message they want to view 
  2. The system redirects the user to the message page 
  3. The message is displayed 
  4. The user can see the message 


- **Primary Postconditions:**
  The user can see the message 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>

  1. The user clicks on the message 
  2. The message is not found 
  3. The system redirects the user to an error page


6. Search for other users (Sherif) 
- **Pre-condition:**
  1. User is logged into their account

- **Trigger:**
  User clicks the "Search" button 

- **Primary Sequence:**
  
  1. User enters the name of the user they want to search for in the text box. 
  2. User clicks the "Search" button. 
  3. System redirects the user to the profile page corresponding to the username. 


- **Primary Postconditions:**
  The user is on the profile page of the searched user

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. User clicks the "Search" button. 
  2. System says "No users found" 
  3. User enters the name of the user they want to search for in the text box. 
  4. User clicks the "Search" button. 
  5. System redirects the user to the profile page corresponding to the username.





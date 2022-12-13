## Functional Requirements

1. Login (Isabel) done
2. Logout (Sherif) done
3. Create a new account (Isabel) done
4. Delete account (Isabel) done
5. View user home page (user can see messages of users they follow) (Bhargavi)
6. Send public messages to followers (may include images) (Bhargavi)
7. Send/receive private messages (Sherif)
8. View followers (Sherif)
9. Edit user's profile. (Isabel) done
10. View a user profile. (Isabel) done
11. Follow other users. (Sherif)
12. Search for other users. (Isabel) done

## Non-functional Requirements
 
1. The system login must be secure (entering the wrong password/username means the user is denied access).
2. The system is expected to support only desktop.
3. The system is expected to work on Mac/Windows/Linux.
4. The system is expected to work on Google Chrome.

## Use Cases

1. Follow other users (Isabel)
- **Pre-condition:**
  1. User must be signed in.

- **Trigger:**
  1. User clicked on "Follow" button.

- **Primary Sequence:**
  
  1. User searches for another user's username (ex: @user2).
  2. System redirects user to the other user's profile picture. (ex: go to user2's profile)
  3. User clicks the "Follow" button.
  4. System adds the other user to list of user's following list. (ex: adds user2 into user's following list)
  5. System refreshes the page (redirects user to the other user's page again) and changes the "Follow" button to "Following".

- **Primary Postconditions:**
  The user is following another user and can see the followed user's content on the home page.

2. View user's profile (Isabel)
- **Pre-condition:** 
  1. User is logged into their account.

- **Trigger:** 
  User clicks on another user's username OR searches for an existing username OR clicks on the "My Profile" button.

- **Primary Sequence:**
  
  1. User clicks on another user's username.
  2. System redirects user to the profile page corresponding to the username.

- **Primary Postconditions:** 
  The user is on a profile page.

- **Alternate Sequence:** 
  
  1. User clicks on the "My Profile" button.
  2. System redirects the user to their profile page.

- **Alternate Sequence:** 
  
  1. User searches for a user with an existing username.
  2. System redirects the user to the other user's profile page.

3. View User Home page (Bhargavi)
- **Pre-condition:** 
  1. User must be logged in

- **Trigger:** 
  User Clicks on "home page" button

- **Primary Sequence:**
  
  1. User clicks on the "home page" button
  2. System redirects user to their homepage.

- **Primary Postconditions:**
  User is on their home page and is able to see messages from other users.

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


5. Send/receive private message (Sherif) 
- **Pre-condition:** 
  1. The user must be logged in 
  2. The user must be on a another user's profile page.


- **Trigger:** 
  User clicks "Send" to trigger send private message.

- **Primary Sequence:**
  
  1. The user clicks "Message" button on another user's profile page.
  2. The system redirects the user to the chatting page and loads all messages between user and the user they want to message
  3. User enters in a message and clicks "Send" button
  4. System sends the message


- **Primary Postconditions:**
  The user can see the messages sent and have sent their desired message if the message is valid.

- **Alternate Sequence:** 

  1. The user clicks "Message" button on another user's profile page.
  2. The system redirects the user to the chatting page and loads all messages between user and the user they want to message
  3. User enters a bad input (ex: just spaces or nothing) but clicks the "Send" button.
  4. System sends nothing and refreshes the page (redirects user to the chatting page and loads all messages again)


6. Search for other users (Sherif) 
- **Pre-condition:**
  1. The user is logged into their account

- **Trigger:**
  User clicks the "Search" button 

- **Primary Sequence:**
  
  1. User enters the username of the user they want to search for in the text box on top of the page. 
  2. User clicks the "Search" button. 
  3. System redirects the user to the profile page corresponding to the username. 


- **Primary Postconditions:**
  The user is on the user profile page of the searched username.

- **Alternate Sequence:**
  
  1. User enters an invalid/ nonexistent username and clicks the "Search" button. 
  2. System redirects user to a page that reads "No users found."
  3. User enters the username they want to search for in the text box on top of the page. 
  4. User clicks the "Search" button. 
  5. System redirects the user to the profile page corresponding to the username.

- **Alternate Sequence:**
  
  1. User enters nothing and clicks the "Search" button. 
  2. System redirects user to an "Invalid search" error page.

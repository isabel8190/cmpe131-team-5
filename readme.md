# Shine - Social Media App

### Created by CMPE131 Team 5
- Bhargavi Datye (@Bhargavi-Datye) bhargavi.datye@sjsu.edu  (team lead)
- Isabel Luong (@isabel8190) isabel.luong@sjsu.edu
- Sherif Philips (@captainsphilips) sherif.philips@gmail.com

## Introduction
Shine is a social media app where you can create an account, follow other users, create posts for your followers to see, and send messages.

## Table of Contents
* [Ethical Implications] (#ethical-implications)
* [Technologies] (#technologies)
* [Required Libraries] (#required-libraries)
* [Launching the App] (#launching-the-app)
* [Starting and Using the App] (#starting-and-using-the-app)
* [Implementation Credits] (#implementation-credits)

## Ethical Implications

As software students, it is our responsibility to ensure that the social media application we are creating meets ethical standards, as well as professional standards. We must ensure that the application meets the highest ethical standards, and that it is designed in a way that minimizes any negative impacts it may have on global, economic, environmental, and societal contexts.

Ethically, we must ensure that the application is designed in a way that respects the privacy of its users. We must ensure that users have the ability to control their data and that any security measures are in place to protect their data from unauthorized access. We must also ensure that the application is designed in a way that is free of discrimination and bias, and that it respects the rights of its users.

Professionally, we must ensure that the application is designed in a way that is secure and reliable. We must also ensure that the application is designed in a way that is easy to use and understand, and that it is designed with scalability in mind.

Additionally, we must ensure that the application is designed in a way that has minimal negative impacts on global, economic, environmental, and societal contexts. We must consider any potential unintended consequences that may arise from the application and take steps to prevent them. This may include ensuring that the application is designed in a way that minimizes its impact on the environment and that it adheres to international laws and regulations.

Overall, it is our responsibility to ensure that the social media application we are creating is designed in a way that meets ethical and professional standards, and that has minimal negative impacts on global, economic, environmental, and societal contexts.

## Technologies
This application was made using the languages listed below.
- Python
- HTML
Therefore, please install Python on your computer before proceeding or use an IDE like Virtual Studio Code. Also, please ensure that you have pip installed. If not, please install it.

## Required Libraries
To run this app you will need the following libraries:
* SQL Alchemy
* Flask
* Flask Login
* Flask Migrate
* Flask wtf
* wtforms
* wekzeug

Therefore, in your terminal, use the following commands:

```
$ pip install flask-sqlalchemy
$ pip install flask
$ pip install flask-wtf
$ pip install wtforms
$ pip install flask-migrate
$ pip install flask-login
$ pip install werkzeug
```

## Launching the App
To run this project please download all files from the GitHub Repository. You can also clone the GitHub Repository using the following command in your terminal inside your desired directory.

```
$ git clone https://github.com/isabel8190/cmpe131-team-5.git
```

Open the project folder using the cd command on the terminal. When you can see the run.py file, you can tun the program by using the following command:

```
$ python run.py
--or--
$ python3 run.py 
(depending on your python version)
```

## Starting and Using the App
Now that the app is running, to access the app, click on the link in the terminal or, copy and paste it into your Chrome browser. The link should look like this:
```
 * Running on http://127.0.0.1:5000
```
Upon first load, you will be met with the login page. Please click on "Sign Up Here" on the link below the login form to create an account.

Once your account is made you would be able to login to the application with each use! The appication can be navigated through a combinations of buttons and links. You should get familiar with the navigation bar on top!

Once you are done using the app, on your terminal, use Ctrl + C at the same time and close the application on your Chrome.

Here are some available, working features:

Home: You are automatically here when you first login. In a future update, you will be able to post your messages here and see the messages of those who you follow!

Search: Allows you to search for other users and view their profile page. In a future update, you will be able to follow and follow the user, as well as send private messages to them!

My Profile: Allows you to view your own profile! 
    Edit: You can edit your own profile which consists of your username and bio, as well as your password! Please make sure to verify all changes using your current password! 
    
    Delete Account: You can also delete your account here, if you wish to do so. :(
    
    In future updates, you can so view your follower and following count, as well as who exactly is following you and who you are following!

Logout: Allows you to log out of your account. You can reaccess your account by logging in.

## Implementation Credits
1. Login                                Completed by Isabel
2. Logout                               Completed by Sherif
3. Create a new account                 Completed by Isabel
4. Delete account                       Completed by Isabel
5. View user home page (user can see messages of users they follow)
6. Send public messages to followers (may include images)
7. Send/receive private messages 
8. View followers
9. Edit user's profile.                 Completed by Isabel
10. View a user profile.                Completed by Isabel
11. Follow other users. (Sherif)
12. Search for other users.             Completed by Isabel
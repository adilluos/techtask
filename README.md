# Technical task on Python Django

Simple technical task, using Python Django, DRF. 
In this project I tried to develop a user profile page with authorization,
activity center and methods of security

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Code Explanations for Other Developers](#code-explanations-for-other-developers)

## Introduction

I am entering the programming world and try to learn new skills on writing backend services. 
In this program I wanted to develop a simple website where user can create, read, update, and delete
information of his profile page. Also user can monitor his activity center.

## Technologies Used

- Django: [Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- Django Rest Framework: [Django Rest Framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs in Django.
- Django REST Framework SimpleJWT: [Django REST Framework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/) provides a JSON Web Token authentication backend for the Django REST Framework.

## Installation

To use this project locally, follow these steps:

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Install the required dependencies using pip and the `requirements.txt` file: pip install -r requirements.txt
4. Apply migrations to set up the database: python manage.py migrate
5. Finally, start the development server: python manage.py runserver
6. The project will now be accessible locally at `http://localhost:8000/`.

## API Documentation for Frontend

1. User Registration
URL: /registration
Method: POST
Parameters:
username (string): User's username.
email (string): User's email.
password (string): User's password.
password2 (string): Re-entered password for confirmation.
Description: Registers a new user.
Response: Upon successful registration, redirects to the settings page (settings). In case of errors (e.g., incorrect input data), displays corresponding error messages.

2. User Login
URL: /login
Method: POST
Parameters:
username (string): User's username.
password (string): User's password.
Description: Authenticates the user and generates JWT tokens for authentication.
Response: Upon successful login, redirects to the profile page (profilepage). In case of errors (e.g., incorrect username or password), displays an appropriate error message.

3. User Logout
URL: /logout
Method: GET
Description: Logs the user out of their account and invalidates JWT tokens.
Response: Upon successful logout, redirects to the login page (login).

4. View User Profile
URL: /profilepage
Method: GET
Description: Displays information about the current user.
Response: Page with information about the current user's profile.

5. Edit Profile Settings
URL: /settings
Method: GET (displays the form for editing settings), POST (saves the changes)
Parameters:
profileimg (image): User's avatar.
name (string): User's name.
surname (string): User's surname.
age (number): User's age.
phone_number (string): User's phone number.
profession (string): User's profession.
about_me (string): User's self-description.
Description: Allows the user to modify their information.
Response: Upon successful changes, displays a message confirming successful settings update. In case of errors, displays error messages.

6. View Activity History
URL: /activity
Method: GET
Description: Displays the user's activity history.
Response: Page with records of user actions (e.g., logins and logouts).

7. JWT Token Authentication
Description: JWT tokens are used for authentication in this API. Upon successful login or registration, the server generates JWT tokens, which are then included in subsequent requests for authentication. The access token is used to authenticate API requests, while the refresh token is used to obtain new access tokens when they expire. Upon logout, the server invalidates the refresh token to ensure the user is logged out securely.

## Code Explanations for Other Developers

Profile Model:
The Profile model represents a user's profile and contains basic information about them, such as name, surname, email, phone number, etc.
Each profile is associated with a user from the Django User model through the user field.
The model also contains methods for managing the profile, such as __str__ to return the user's name.

ProfileHistory Model:
The ProfileHistory model represents the user's action history and contains records of various actions, such as logins and logouts.
Each history record is associated with the user's profile through the foreign key user_profile.
The model contains fields for the type of action (activity_type), timestamp (timestamp), and additional details (details).

Views:
Views in the views.py file handle requests from users and return corresponding responses, including HTML pages and redirects.
Views implement the logic for registration, login, logout, viewing and editing user profiles, as well as viewing activity history.
Decorators like login_required are used to ensure security of views by requiring authentication.

API Views:
API views in the api.py file are used to provide data about user profiles and action history in JSON format.
Django REST Framework is used to create the API and automatically serialize model data into JSON format.
API views include CRUD (Create, Read, Update, Delete) operations for user profiles and action history.

# blog_permissions


This project make it possible for users to login and also register as new user, a user can only view the blog post only when they are not logged in, but once logged in they can as well create,update,delete their own blog post only.

# Setup and Installation
*Note**: Make sure to download/clone this repository and navigate to the folder in your terminal. Now follow the instructions below

Create the virtual environment.
virtualenv /path/to/venv --python=/path/to/python3
You can find out the path to your python3 interpreter with the command which python3.

Set up .env file by duplicating the .env file(and editing if required).

Activate the environment and install dependencies.

Linux
source /path/to/venv/bin/activate
pip install -r requirements.txt

Windows
./path/to/venv/bin/activate
pip install -r requirements.txt
Launch the app

python manage.py runserver localhost:8000

# Prerequisites

Python 3.10.4 Download
Django
Django rest_framework
Heroku Account Signup
A working django Project. If you don't have one you can clone this
virtualenv or an alternative

# REFERENCES

Django
DRF
Python Decouple
python Pillow==9.1.1
python database_url
Gunicorn
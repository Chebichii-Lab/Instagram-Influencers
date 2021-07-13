# INSTAGRAM INFLUENCERS!

## Author
Natasha Serem.

### Description
This is a Django Instagram clone application where, a user can sign up to have a profile in the application. The user can also view comments, comment, like and post on the application. 

## Setup and Installations
To get the code, clone the repository: https://github.com/Chebichii-Lab/Instagram-Influencers.git
Move to the folder and run the following commands;

    $ cd Instagram-Influencers
    $ pip install -r requirements.txt

### Install and activate the virtual environment
    $ python3.8 -m venv virtual
    $ source virtual/bin/activate

### Create a database
    $ psql
CREATE DATABASE (name-of-database)

### Make migrations
    $ python3.8 manage.py check
    $ python3.8 manage.py makemigrations (app-name)
    $ python3 manage.py migrate

### Testing the Application
    $ python3.8 manage.py test (app-name)

### Running the Application
    $ python3.8 manage.py runserver

Then once you are done, open your browser with the local host; 127.0.0.1:8000

## Dependencies
1. Python3.8
2. Django 1.11.17
3. Virtual environment. To install Virtual Environment, run this code; $ python3.8 -m venv virtual
4. Heroku
5. Gunicorn

## Technologies used
1. Python 3.8.10
2. HTML
3. Django 3.2.5
4. Bootstrap 3
5. Heroku
6. Postgresql

# Live Link

[View Live Site.](https://insta254.herokuapp.com/)

## License

Instagram2.0 clone is under the [MIT](LICENSE) license.








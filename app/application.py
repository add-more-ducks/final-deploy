'''
Thomas van Genderen - Spring 2021
Main application file
'''

from flask import Flask, session, redirect, url_for, render_template, request, jsonify, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_socketio import SocketIO, emit
# refers to forms.py
from forms import RegistrationForm, LoginForm
from markupsafe import escape
import os

from models import *

import json
import os

# Configure Flask App
app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configure session, use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure migrations
Migrate(app, db)

# for integrating admin section (webapp site UvA) 
# different in tutorial
app.secret_key = os.environ['SECRET_KEY']
#admin = Admin(app, name='Timeline Admin', template_mode='bootstrap3')
#admin.add_view(ModelView(User, db.session))
#admin.add_view(ModelView(Item, db.session))

# Configure login_manager
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'
#login_manager.login_message = 'You really need to log in!'

#@login_manager.user_loader
#def load_user(user_id):
    # might need to change to return User.get(user_id)
#    return User.query.get(int(user_id))

# From youtube tutorial pt2. 

posts = [
            {
                "media": {
                "url": "",
                "caption": "",
                "credit": ""
                },
                "start_date": {
                "month": "4",
                "day": "30",
                "year": "2021"
                },
                "text": {
                "headline": "The first local JSON appears on the timeline",
                "text": "<p>After a lot of effort and frustration, I asked Kiara for elp and she found out how to feed JSON to the timeline.</p>"
                }
            },
            {
                "media": {
                "url": "",
                "caption": "",
                "credit": ""
                },
                "start_date": {
                "month": "",
                "day": "",
                "year": "2019"
                },
                "end_date": {
                "month": "",
                "day": "",
                "year": "2022"
                },
                "text": {
                "headline": "Start of Covid19",
                "text": ""
                }
            },
            {
                "media": {
                "url": "",
                "caption": "",
                "credit": "",
                "thumbnail": "",
                "alt": "",
                "title": "",
                "link": "",
                "link_target": ""
                },
                "start_date": {
                "year": "2019",
                "month": "",
                "day": "",
                "hour": "",
                "minute": "",
                "second": "",
                "millisecond": "",
                "display_date": ""
                },
                "end_date": {
                "year": "2020",
                "month": "",
                "day": "",
                "hour": "",
                "minute": "",
                "second": "",
                "millisecond": "",
                "display_date": ""
                },
                "text": {
                "headline": "Start of Covid19",
                "text": ""
                }
            }
        ]


# Display the homepage
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', posts=posts, titl='about')


# Get called from register.js to verify uniqueness of new username
@app.route('/confirmation', methods=['POST'])
def confirmation():
    username = request.form.get("username")
    taken = User.query.filter_by(username=username).first()

    print(taken)
    if taken:
        return jsonify({'success': False})
    
    return jsonify({'success': True})


# Create a new User object or just display the page for user to input data
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
#    if form.validate_on_submit()
    return render_template('register.html', title='Register', form=form)

"""    
    # ensure no current session
    session.clear()

    if request.method == "GET":
        return render_template("register.html")
    
    else:        
        # request input of the form
        username = request.form.get("username")
        password = request.form.get("password")

        user = User(username = username, password = password)

        db.session.add(user)
        db.session.commit()
        
        return render_template('/login.html')


# Display input page for loggin in
# from https://flask-login.readthedocs.io/en/latest/#installation
@app.route('/login', methods=['GET'])
def login():
    return render_template("/login.html")

"""
# Create a new User object or just display the page for user to input data
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # temporary verification requirements CHANGE THIS
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccesful. Please check username and password', 'danger')        
    return render_template('login.html', title='Login', form=form)


# Log user in if input is adequate
@app.route('/logmein', methods = ['POST'])
def logmein():
    username = request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if not user:
        return 'User not found!'
    login_user(user, remember=True) 
    return redirect("/")

# Clear current session and log out user
@app.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect("/")


@app.route("/timeline")
def timeline():
    return render_template('timeline.html')

@app.route("/french")
def french():
    return render_template('frans.html')

@app.route("/test")
def test():
    return render_template('test.html')


# main starting command
if __name__ == "__main__":
#    main()
# The above line works. Can run instead of the one below.
    app.run(debug=True)

# call with: $ python application.py 
# instead of flask run
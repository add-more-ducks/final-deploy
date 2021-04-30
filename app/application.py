'''
Thomas van Genderen - Spring 2021
Main application file
'''

from flask import Flask, session, redirect, url_for, render_template, request, jsonify
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_socketio import SocketIO, emit
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
#app.secret_key = os.environ['SECRET_KEY']
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


# Display the homepage
@app.route("/")
def index():
    return render_template('index.html')

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
@app.route("/register", methods=["GET", "POST"])
def register():
    
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
def tijdslijn():
    return render_template('timeline.html')

@app.route("/frans")
def french():
    return render_template('frans.html')

@app.route("/test")
def testing():
    return render_template('test.html')

if __name__ == "__main__":
    main()
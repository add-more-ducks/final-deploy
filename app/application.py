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
from markupsafe import escape
import os

# Configure Flask App
app = Flask(__name__)

if not os.getenv("DATABSE_URL"):
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

# Display the homepage
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/timeline")
def tijdslijn():
    return render_template('timeline.html')

if __name__ == "__main__":
    main()
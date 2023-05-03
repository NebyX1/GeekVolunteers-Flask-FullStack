from flask import request, jsonify, render_template, redirect, url_for, flash
from models.tables import Users
from database.db import db
# from helpers.forms import LoginForm
# from flask_login import login_user, logout_user, login_required, LoginManager
import json
from flask import jsonify
from datetime import timedelta
from flask import make_response
from werkzeug.utils import secure_filename
from flask import current_app


# login_manager = LoginManager()


def init_app(app):

    # login_manager.init_app(app)

    @app.route("/")
    @app.route("/index")
    @app.route("/home")
    def home_page():
        return render_template('home.html')
from urllib import response
from flask import Blueprint, jsonify, request, current_app
from flask_login import current_user, login_user, logout_user
from sqlalchemy import exc, asc, desc
from werkzeug.security import check_password_hash

from app.models.usersModel import UsersModel
from app.forms.usersForm import UsersValidation
from app import db

from app.utils.utils import get_blank_response, extract_query_arguments


mod = Blueprint("accountsView", __name__)


@mod.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated():
        return "user already logged in"
    
    validation_result = UsersValidation.validate(request.get_json())
    if validation_result[0]:
        user = db.session.query(UsersModel).filter_by(username=request.args["username"]).first()
        if user is None or check_password_hash(user["password_hash"], request.args["password"]):
            return "Invalid username or password"
        login_user(user)


@mod.route("/logout")
def logout():
    logout_user()
    return "logged out"

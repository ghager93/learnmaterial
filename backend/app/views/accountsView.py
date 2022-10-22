import re
from urllib import response
from flask import Blueprint, jsonify, request, current_app
from flask_login import current_user, login_user, logout_user, login_manager
from sqlalchemy import exc, asc, desc
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.user import UsersModel
from app.forms.usersForm import UsersValidation
from app import db

from app.utils.utils import get_blank_response, extract_query_arguments


mod = Blueprint("accountsView", __name__)


@mod.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        return "user already logged in"
    
    payload = request.get_json()

    validation_result = UsersValidation.validate(payload)
    if validation_result[0]:
        user = db.session.query(UsersModel).filter_by(username=payload["username"]).first()
        if user is None or not check_password_hash(user.password_hash, payload["password"]):
            return "Invalid username or password"
        login_user(user)
        return "logged in", 200
    current_app.logger.debug("Payload validation error")
    current_app.logger.debug(validation_result[1])
    return (
        jsonify(
            {
                "error": {
                    "code": 404,
                    "message": f"Payload validation error: {validation_result[1]}",
                    "payload": str(payload)
                }
            }
        ), 404
    )


@mod.route("/logout")
def logout():
    logout_user()
    return "logged out", 200

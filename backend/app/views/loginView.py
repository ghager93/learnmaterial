from operator import methodcaller
from flask import Blueprint, jsonify, request, current_app
from flask_login import login_manager, login_user

from app import db
from app.models.usersModel import UsersModel

mod = Blueprint("loginView", __name__)

@login_manager.user_loader
def load_user(user_id):
    return UsersModel.query.get(int(user_id))

@mod.route("/", methods=["POST"])
def login():
    try:
        user = db.session.query(UsersModel).filter_by(username=request.get_json()["username"]).first()
        login_user(user)
    except:
        return 404
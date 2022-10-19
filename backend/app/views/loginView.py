from operator import methodcaller
from flask import Blueprint, jsonify, request, current_app
# from flask_login import login_manager, login_user
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from app import db, login_manager
from app.models.usersModel import UsersModel

mod = Blueprint("loginView", __name__)


@login_manager.user_loader
def load_user(user_id):
    return UsersModel.query.get(int(user_id))


@login_manager.request_loader
def load_user_from_request(request):
    ...

@mod.route("/", methods=["POST"])
def login():
    try:
        user = db.session.query(UsersModel).filter_by(username=request.json.get("username", None)).first_or_404()

        if user.verify_password(request.json.get("password", None)):
            return {"token": create_access_token(identity=user)}

        raise Exception("Incorrect password")
    except Exception as e:
        return {"error": str(e)}, 404
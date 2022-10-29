from datetime import datetime
from tokenize import Token
from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, set_access_cookies, get_jwt

from app import db, jwt_manager
from app.models.user import User
from app.models.token_block_list import TokenBlockList


mod = Blueprint("loginView", __name__)

@jwt_manager.token_in_blocklist_loader
def is_token_blocked(jwt_header, jwt_payload):
    token = db.session.query(TokenBlockList).filter_by(jti=jwt_payload["jti"]).scalar()
    return token is not None


@mod.route("/login", methods=["POST"])
def login():
    try:
        user = db.session.query(User).filter_by(username=request.json.get("username", None)).first_or_404()

        if user.verify_password(request.json.get("password", None)):
            access_token = create_access_token(identity=user)
            response = jsonify({"msg": "Logged in."})
            set_access_cookies(response, access_token)

            return response

        raise Exception("Incorrect password")
    except Exception as e:
        return {"error": str(e)}, 404


@mod.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    try:
        row = TokenBlockList(
            jti=get_jwt()['jti'],
            created_at=datetime.utcnow()
        )
        db.session.add(row)
        db.session.commit()

        return "Logged out", 200 
    except Exception as e:
        return f"Error {str(e)}", 500

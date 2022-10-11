from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from app.models.testModel import TestModel
from app import db


mod = Blueprint("testView", __name__)

@mod.route('/')
def baseRoute():
    return {"data": "This is the base route."}

@mod.route('/test', methods=['GET'])
def get_all_test():
    response = {
        "data": []
    }

    try:
        rows = db.session.query(TestModel).filter_by(**request.args).all()
    except exc.InvalidRequestError as e:
        return (
            jsonify({"error": {"code": 400, "message": "Invalid query parameter"}}),
            400
        )
    if rows:
        response["data"].append([row.to_dict() for row in rows])
        return jsonify(response), 200
        
    return (
        jsonify({"error": {"code": 400, "message": "No entries."}}),
        400
    )


@mod.route('/test', methods=['POST'])
def create_test():
    response = {
        "data": []
    }

    js = request.get_json()

    row = TestModel(**js)
    
    try:
        db.session.add(row)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return (jsonify(
                {
                    "error": {
                        "code": 400,
                        "message": str(e),
                        "payload": str(request.data)
                    }
                }
            ),
            400
        )
    else:
        # Row was added lets send the response payload with the row we added
        response["data"].append(row.to_dict())
        return jsonify(response), 201
        
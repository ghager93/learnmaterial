from flask import Blueprint, jsonify, request, current_app
from sqlalchemy import exc, asc, desc

import youtubeApi

from app.models.videosModel import VideosModel
from app.forms.videosForm import VideosValidation
from app import db

from app.utils.queries import get_all_query, get_query
from app.utils.responses import data_items_template, error


mod = Blueprint("videosView", __name__)


def _build_row(payload):
    youtube_data = youtubeApi.get_video_data(payload['id'])

    return VideosModel(
        name=payload['name'],
        title=youtube_data.title,
        author=youtube_data.channel_title,
        description=youtube_data.description,
        link=payload['link'],
        timestamp=payload['timestamp'],
        tags=youtube_data.tags,
        length=youtube_data.duration
    )


@mod.route("/", methods=["GET"])
def get_all():
    '''
    Returns all resources.
    '''
    response = data_items_template()

    current_app.logger.debug(f"Received GET request to {request.path}, about to query database")

    try:
        rows = get_all_query(db, VideosModel, request.args)
    except exc.InvalidRequestError as e:
        return error(400, "Invalid query parameter")
    if rows:
        current_app.logger.debug(f"Database response {[row.to_dict() for row in rows]}")
        [response["data"]["items"].append(row.to_dict()) for row in rows]
        return jsonify(response), 200
    else:
        current_app.logger.debug(f"No entries")
        return (
            jsonify({"error": {"code": 404, "message": "No entries"}}),
            404,
        )


@mod.route("/<id>", methods=["GET"])
def get(id):
    """
    Returns resource with given id.
    """
    response = data_items_template()

    current_app.logger.debug(f"Received GET request to {request.path}, about to query database")

    try:
        row = get_query(db, VideosModel, id)
    except exc.InvalidRequestError as e:
        return error(400, "Invalid query parameter")
    if row:
        current_app.logger.debug(f"Database response {row}")
        response["data"]["items"].append(row.to_dict())
        return jsonify(response), 200
    else:
        current_app.logger.debug(f"No entries for ID: {id}")
        return (
            jsonify({"error": {"code": 404, "message": "No entries for given ID"}}),
            404,
        )


@mod.route("/", methods=["POST"])
def create():
    """
    Create a resource in the database.
    """
    response = data_items_template()

    current_app.logger.debug(f"request payload: {request.get_json()}")

    validation_result = VideosValidation.validate(request.get_json())
    current_app.logger.debug(f"Validation result: {validation_result}")
    if validation_result[0]:
        js = request.get_json()
        row = _build_row(js)
        try:
            current_app.logger.debug(f"Attempting to add row to db: {row}")
            db.session.add(row)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            # some thing went wrong when writing to db, send the error payload.
            current_app.logger.error(f"Could not write row to db")
            current_app.logger.error(e)
            db.session.rollback()
            return (
                jsonify(
                    {
                        "error": {
                            "code": 400,
                            "message": str(e),
                            "payload": str(request.data),
                        }
                    }
                ),
                400,
            )
        else:
            # Row was added lets send the response payload with the row we added
            response["data"]["items"].append(row.to_dict())
            return jsonify(response), 201
    else:
        current_app.logger.debug("Payload validation error")
        current_app.logger.debug(validation_result[1])
        db.session.rollback()
        return (
            jsonify(
                {
                    "error": {
                        "code": 403,
                        "message": f"Payload validation error: {validation_result[1]}",
                        "payload": str(request.data)
                    }
                }
            ),
            403
        )


@mod.route("/<id>", methods=["DELETE"])
def delete(id):
    """
    Deletes resource for given id.
    """
    response = data_items_template()

    current_app.logger.debug(f"Received  DELETE request to {request.path}, about to query database")

    row = db.session.query(VideosModel).filter_by(id=id).first()
    if row:
        try:
            current_app.logger.debug(f"Database response {row.to_dict()}")
            current_app.logger.debug(f"About to attempt to delete row")
            db.session.delete(row)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            # some thing went wrong when writing to db, send the error payload.
            current_app.logger.error("Something went wrong when deleting row")
            current_app.logger.error(e)
            db.session.rollback()
            return (
                jsonify(
                    {
                        "error": {
                            "code": 400,
                            "message": str(e),
                            "payload": str(request.data),
                        }
                    }
                ),
                400,
            )
        else:
            resp_data = row.to_dict()

            # we want to add deleted: true to the object we return.
            resp_data["deleted"] = "true"  
            response["data"]["items"].append(resp_data)
            current_app.logger.debug(f"Row deleted: {resp_data}")
            return jsonify(response), 201
    else:
        return (
            jsonify({"error": {"code": 404, "message": "No entry for given ID"}}),
            404,
        )


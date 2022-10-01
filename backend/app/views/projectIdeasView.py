from flask import Blueprint, jsonify, request, current_app
from sqlalchemy import exc, asc, desc

from app.models.projectIdeasModel import ProjectIdeasModel
from app.forms.projectIdeasForm import ProjectIdeasValidation
from app import db

from app.utils.utils import get_blank_response, extract_query_arguments


mod = Blueprint("projectIdeasView", __name__)


@mod.route("/", methods=["GET"])
def get_all():
    '''
    Returns all resources.
    '''
    response = get_blank_response()

    current_app.logger.debug(f"Received GET request to {request.path}, about to query database")

    args = extract_query_arguments(request.args)
    sort_arg = (
        asc(args.sort_by) if args.sort_order == "ascending" else desc(args.sort_by)
    )

    try:
        rows = (
            db.session.query(ProjectIdeasModel)
            .filter_by(**args.filter_dict)
            .order_by(sort_arg)
            .paginate(page=args.page, per_page=args.per_page, error_out=False)
            .items
        )
    except exc.InvalidRequestError as e:
        return (
            jsonify({"error": {"code": 400, "message": "Invalid query parameter"}}),
            400,
        )
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
    response = get_blank_response()

    current_app.logger.debug(f"Received GET request to {request.path}, about to query database")

    args = extract_query_arguments(request.args)
    sort_arg = (
        asc(args.sort_by) if args.sort_order == "ascending" else desc(args.sort_by)
    )
    
    try:
        row = db.session.query(ProjectIdeasModel).filter_by(id=id).first()
    except exc.InvalidRequestError as e:
        return (
            jsonify({"error": {"code": 400, "message": "Invalid query parameter"}}),
            400,
        )
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
    response = get_blank_response()

    current_app.logger.debug(f"request payload: {request.get_json()}")

    validation_result = ProjectIdeasValidation.validate(request.get_json())
    current_app.logger.debug(f"Validation result: {validation_result}")
    if validation_result[0]:
        js = request.get_json()
        row = ProjectIdeasModel(**js)
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
    response = get_blank_response()

    current_app.logger.debug(f"Received  DELETE request to {request.path}, about to query database")

    row = db.session.query(ProjectIdeasModel).filter_by(id=id).first()
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


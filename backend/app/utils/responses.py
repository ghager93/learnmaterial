from flask import jsonify


def data_items_template():
    return {'data': {'items': []}}


def rest_response(response, code):
    return jsonify(response), code


def error(message, code):
    return (
        jsonify({"error": {"code": code, "message": message}}),
        code
    )
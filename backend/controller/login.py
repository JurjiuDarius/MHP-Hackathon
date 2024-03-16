from flask import Blueprint, request, jsonify
from service import authentication_service

login_blueprint = Blueprint("login", __name__, url_prefix="/login")


@login_blueprint.route("/", methods=["POST"])
def login():
    data = request.json
    result, status = authentication_service.login(data)
    return jsonify(result), status

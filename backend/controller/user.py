from flask import Blueprint, request, jsonify
from models import User
from service.user_service import get_users as service_get_users

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("/users", methods=["GET"])
def get_users():
    return jsonify(service_get_users())

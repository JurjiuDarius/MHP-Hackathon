from flask import Blueprint, request, jsonify
from models import User
from service.user_service import get_users as service_get_users
from utils.jwt import check_authorization

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@check_authorization(["admin", "user"])
@user_blueprint.route("/users", methods=["GET"])
def get_users():
    return jsonify(service_get_users())

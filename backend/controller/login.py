from flask import Blueprint
from flask import request
from service import authenticatin_service

login_blueprint = Blueprint("login", __name__, url_prefix="/login")


@login_blueprint.route("/", methods=["POST"])
def login():
    data = request.json
    return authenticatin_service.login(data)

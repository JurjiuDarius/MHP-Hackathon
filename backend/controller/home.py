from flask import Blueprint, jsonify

home = Blueprint("home", __name__)


@home.route("/")
def hello_world():
    return jsonify(message="Hello, World!")

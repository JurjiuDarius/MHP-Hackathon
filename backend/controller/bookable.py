from flask import Blueprint, request, jsonify
from service import bookable_service

bookable_blueprint = Blueprint("bookable", __name__, url_prefix="/bookables")


@bookable_blueprint.route("/<string:bookableId>/capacity", methods=["GET"])
def get_capacity(bookableId):
    result, status = bookable_service.get_bookable_capacity(bookableId)
    return jsonify(result), status

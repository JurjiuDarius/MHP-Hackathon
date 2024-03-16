from flask import Blueprint, request, jsonify
from service import statistics_service

statistics_blueprint = Blueprint("statistics", __name__, url_prefix="/statistics")


@statistics_blueprint.route("/office-occupation", methods=["POST"])
def get_office_occupation():
    data = request.json
    result, status = statistics_service.get_office_occupation(data)
    return jsonify(result), status

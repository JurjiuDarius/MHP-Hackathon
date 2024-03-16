from flask import jsonify, request
from flask import Blueprint

from models import Booking
from service import booking_service

booking_blueprint = Blueprint("booking", __name__, url_prefix="/bookings")


@booking_blueprint.route("/", methods=["POST"])
def create_booking():
    try:
        data = request.json
        booking = booking_service.create_booking(
            data["user_id"],
            data["bookable_id"],
            data["date"],
            data["start"],
            data["end"],
            data["people"],
        )
        return jsonify(booking.serialize()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@booking_blueprint.route("/<int:booking_id>", methods=["GET"])
def get_booking(booking_id):
    booking = booking_service.get_booking(booking_id)
    if booking:
        return jsonify(booking)
    else:
        return jsonify({"error": "Booking not found"}), 404


@booking_blueprint.route("/<int:booking_id>", methods=["PUT"])
def update_booking(booking_id):
    try:
        data = request.json
        booking = booking_service.update_booking(
            booking_id,
            data.get("room_id"),
            data.get("date"),
            data.get("start"),
            data.get("end"),
        )
        return jsonify(booking)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@booking_blueprint.route("/<int:booking_id>", methods=["DELETE"])
def delete_booking(booking_id):
    try:
        booking_service.delete_booking(booking_id)
        return "", 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@booking_blueprint.route("/", methods=["GET"])
def get_all_bookings():
    all_bookings = booking_service.get_all_bookings()

    return jsonify(all_bookings)


@booking_blueprint.route("/filter-by-date/", methods=["POST"])
def filter_bookings_by_date():
    booking_date = request.json["date"]
    bookings = booking_service.filter_bookings_by_date(booking_date)
    return jsonify(bookings), 200


@booking_blueprint.route("/user/<int:user_id>", methods=["GET"])
def get_bookings_for_user(user_id):
    bookings, status = booking_service.get_bookings_for_user(user_id)
    return jsonify(bookings), status

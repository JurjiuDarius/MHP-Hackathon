from flask import jsonify, request
from flask import Blueprint

from models import Booking
from service import booking_service

booking = Blueprint("booking", __name__, url_prefix="/bookings")


@booking.route('/', methods=['POST'])
def create_booking():
    try:
        data = request.json
        booking = booking_service.create_booking(data['user_id'], data['room_id'], data['date'], data['start'],
                                                 data['end'])
        return jsonify(booking), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@booking.route('/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = booking_service.get_booking(booking_id)
    if booking:
        return jsonify(booking)
    else:
        return jsonify({'error': 'Booking not found'}), 404


@booking.route('/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    try:
        data = request.json
        booking = booking_service.update_booking(booking_id, data.get('room_id'), data.get('date'),
                                                 data.get('start'), data.get('end'))
        return jsonify(booking)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@booking.route('/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    try:
        booking_service.delete_booking(booking_id)
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@booking.route('/', methods=['GET'])
def get_all_bookings():
    all_bookings = Booking.query.all()

    bookings_list = []
    for booking in all_bookings:
        booking_data = {
            'id': booking.id,
            'user_id': booking.user_id,
            'room_id': booking.room_id,
            'date': booking.date,
            'start': booking.start_time,
            'end': booking.end_time
        }
        bookings_list.append(booking_data)

    return jsonify(bookings_list)


@booking.route('/filter-by-date', methods=['GET'])
def filter_bookings_by_date():
    date = request.args.get('date')
    bookings = booking_service.filter_bookings_by_date(date)
    return jsonify(bookings)

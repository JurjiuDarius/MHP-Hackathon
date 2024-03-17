import unittest
from unittest.mock import MagicMock, patch
import datetime
from service.bookable_service import get_bookable_capacity, get_bookable_availability, get_bookable_colors


class TestBookableService(unittest.TestCase):

    @patch('service.bookable_service.Room.query.get')
    def test_get_bookable_capacity_room_found(self, mock_room_query):
        mock_room_query.return_value = MagicMock(capacity=10)

        bookable_id = 1
        capacity, status_code = get_bookable_capacity(bookable_id)

        self.assertEqual(status_code, 200)
        self.assertEqual(capacity, 10)

    @patch('service.bookable_service.Room.query.get')
    def test_get_bookable_capacity_room_not_found(self, mock_room_query):
        mock_room_query.return_value = None

        bookable_id = 1
        capacity, status_code = get_bookable_capacity(bookable_id)

        self.assertEqual(status_code, 404)
        self.assertEqual(capacity, "Room or desk not found")

    @patch('service.bookable_service.Desk.query.get')
    def test_get_bookable_capacity_desk_found(self, mock_desk_query):
        mock_desk_query.return_value = MagicMock()

        bookable_id = 1
        capacity, status_code = get_bookable_capacity(bookable_id)

        self.assertEqual(status_code, 200)
        self.assertEqual(capacity, 1)

    @patch('service.bookable_service.ai_controller')
    def test_get_bookable_availability(self, mock_ai_controller):
        mock_ai = MagicMock()
        mock_ai.get_desk_prediction_morning.return_value = 0.5
        mock_ai.get_desk_prediction_evening.return_value = 0.7
        mock_ai_controller.return_value = mock_ai

        data = {"bookableId": 1, "date": "10/03/2024"}
        availability, status_code = get_bookable_availability(data)

        self.assertEqual(status_code, 200)
        self.assertEqual(availability, ['0.50', '0.70'])


if __name__ == '__main__':
    unittest.main()

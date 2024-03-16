import unittest
from unittest.mock import MagicMock, patch
from service.booking_service import *


class TestMyService(unittest.TestCase):

    def setUp(self):
        self.mock_booking_model = MagicMock()

    def test_create_booking(self):
        mock_booking_class = MagicMock()

        mock_booking = MagicMock()
        mock_booking.user_id = 1
        mock_booking.date = '2024-03-16'
        mock_booking.start = '09:00'
        mock_booking.end = '10:00'
        mock_booking.room_id = 2

        mock_booking_class.return_value = mock_booking

        mock_session = MagicMock()
        mock_session.add = MagicMock()
        mock_session.commit = MagicMock()

        with patch('service.booking_service.Booking', mock_booking_class), \
                patch('service.booking_service.db.session', mock_session):
            booking = create_booking(user_id=1, bookable_id=1, people=['test@example.com'], date='2024-03-16', start='09:00', end='10:00')

            self.assertIsNotNone(booking)
            self.assertEqual(booking.user_id, 1)
            self.assertEqual(booking.room_id, 2)  # Updated assertion
            self.assertEqual(booking.date, '2024-03-16')
            self.assertEqual(booking.start, '09:00')
            self.assertEqual(booking.end, '10:00')

    def test_get_booking(self):
        self.mock_booking_model.query.get.return_value = MagicMock(id=1, user_id=1, date='2024-03-16',
                                                                   start='09:00', end='10:00')

        with patch('service.booking_service.Booking', self.mock_booking_model):
            booking = get_booking(1)

            self.assertIsNotNone(booking)
            self.assertEqual(booking.id, 1)
            self.assertEqual(booking.user_id, 1)
            self.assertEqual(booking.date, '2024-03-16')
            self.assertEqual(booking.start, '09:00')
            self.assertEqual(booking.end, '10:00')

            self.mock_booking_model.query.get.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()

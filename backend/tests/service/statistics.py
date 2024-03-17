import unittest
from unittest.mock import MagicMock, patch
from service.statistics_service import get_office_occupation


class TestOfficeOccupationService(unittest.TestCase):

    @patch('service.statistics_service.get_office_occupation')
    def test_get_office_occupation(self, mock_ai_controller):
        mock_ai = MagicMock()
        mock_ai.get_presence_prediction.return_value = 0.75
        mock_ai_controller.return_value = mock_ai

        data = {"date": "10/03/2024"}
        occupation, status_code = get_office_occupation(data)

        self.assertEqual(status_code, 200)
        self.assertEqual(occupation, 0.75)


if __name__ == '__main__':
    unittest.main()

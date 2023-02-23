import unittest
import json
from app import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_info(self):
        response = self.app.get('/api/info')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('asin', data)
        self.assertIn('brand', data)
        self.assertIn('source', data)
        self.assertIn('stars', data)

    def test_timeline(self):
        # Test with valid parameters
        response = self.app.get(
            '/api/timeline?startDate=2022-01-01&endDate=2022-01-31&Grouping=monthly&Type=cumulative')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('timeline', data)
        self.assertIsInstance(data['timeline'], list)

import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_fact_endpoint(self):
        response = self.client.get("/fact")
        self.assertEqual(response.status_code, 200)
        self.assertIn("fact", response.get_json())

if __name__ == "__main__":
    unittest.main()

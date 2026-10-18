
import unittest
from app.main import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to my DevOps CI/CD Project!", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"healthy", response.data)


if __name__ == "__main__":
    unittest.main()

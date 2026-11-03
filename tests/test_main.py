
import unittest
from app.main import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
<<<<<<< HEAD
        app.config["TESTING"] = True
=======
>>>>>>> 86daa463c7aa66dc5603dfa0c0e8ea7f96c1d1c3
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
<<<<<<< HEAD
        self.assertEqual(
            response.get_json()["project"],
            "Project-1-CICD"
        )
=======
        self.assertIn(b"Welcome to my DevOps CI/CD Project!", response.data)
>>>>>>> 86daa463c7aa66dc5603dfa0c0e8ea7f96c1d1c3

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
<<<<<<< HEAD
        self.assertEqual(
            response.get_json()["status"],
            "healthy"
        )

    def test_greet_with_valid_name(self):
        response = self.client.get("/greet?name=Juveriya")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["message"],
            "Hello, Juveriya!"
        )

    def test_greet_without_name(self):
        response = self.client.get("/greet")
        self.assertEqual(response.status_code, 400)

    def test_greet_with_blank_name(self):
        response = self.client.get("/greet?name=%20%20")
        self.assertEqual(response.status_code, 400)

    def test_greet_with_long_name(self):
        response = self.client.get(
            "/greet",
            query_string={"name": "A" * 51}
        )
        self.assertEqual(response.status_code, 400)
=======
        self.assertIn(b"healthy", response.data)
>>>>>>> 86daa463c7aa66dc5603dfa0c0e8ea7f96c1d1c3


if __name__ == "__main__":
    unittest.main()

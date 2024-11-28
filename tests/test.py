import unittest
import os
from flask import Flask, session
from src.app import app, users
from src.database.db import init_db, DATABASE_PATH
from datetime import timedelta


class TestSessionManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Ensure the database path exists
        os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

    def setUp(self):
        # Set up a test client and initialize the database
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            init_db()

    def test_database_file_exists(self):
        # Check if the database file exists
        if os.path.exists(DATABASE_PATH):
            print("test_database_file_exists: PASSED")
        else:
            print("test_database_file_exists: FAILED")
        self.assertTrue(os.path.exists(DATABASE_PATH), "Database file should exist")

    def test_flask_project_running(self):
        # Check if the Flask app can handle a simple request
        response = self.app.get("/")
        if response.status_code == 302:
            print("test_flask_project_running: PASSED")
        else:
            print("test_flask_project_running: FAILED")
        self.assertEqual(
            response.status_code,
            302,
            "Flask project should be running and redirect to login page",
        )

    def test_authentication_required(self):
        with self.app as client:
            # Try to add a product to the cart without logging in
            response = client.get("/add_to_cart/1")

            # Check if the user is redirected to the login page
            self.assertEqual(
                response.status_code,
                302,
                "User should be redirected to login page when not authenticated",
            )


if __name__ == "__main__":
    unittest.main()

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

    def test_unique_session_id(self):
        with self.app as client:
            # Log in the first time
            client.post(
                "/login", data=dict(username="authorized_user", password="password123")
            )
            old_session_id = session.get("session_id")

            # Log out
            client.get("/logout")

            # Log in the second time
            client.post(
                "/login", data=dict(username="authorized_user", password="password123")
            )
            new_session_id = session.get("session_id")

            # Check if the session ID is different
            self.assertNotEqual(
                old_session_id,
                new_session_id,
                "Session ID should be unique for each login",
            )

    def test_session_timeout(self):
        with self.app as client:
            # Log in and set a short session timeout
            client.post(
                "/login", data=dict(username="authorized_user", password="password123")
            )

            # Wait for the session to expire
            import time

            time.sleep(2)

            # Try to access a protected route after the session should have expired
            response = client.get("/products")
            if response.status_code == 302:
                print("test_session_timeout: PASSED")
            else:
                print("test_session_timeout: FAILED")
            self.assertEqual(
                response.status_code,
                302,
                "User should be redirected to login page after session timeout",
            )


if __name__ == "__main__":
    unittest.main()

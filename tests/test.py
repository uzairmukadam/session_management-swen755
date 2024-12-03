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

if __name__ == "__main__":
    unittest.main()

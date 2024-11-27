import unittest
from flask import Flask, session
from src.app import app, users
from src.database.db import init_db, DATABASE_PATH

class TestSessionManagement(unittest.TestCase):

    def setUp(self):
        # Set up a test client and initialize the database
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            init_db()

if __name__ == '__main__':
    unittest.main()

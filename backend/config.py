import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///trackers.db'  # You can use a more advanced database if needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # Random secret key for session management

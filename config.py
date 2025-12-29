import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if not SQLALCHEMY_DATABASE_URI:
        raise RuntimeError("DATABASE_URL environment variable is not set")


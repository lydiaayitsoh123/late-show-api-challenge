import os
from dotenv import load_dotenv

# Load environment variables from a .env file, if present
load_dotenv()

class Config:
    # PostgreSQL URI using the role and password you just created
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        'postgresql://lydia:okwemba@localhost:5432/late_show_db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for JWT — you must set this in .env or it will raise an error
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    if not JWT_SECRET_KEY:
        raise ValueError("JWT_SECRET_KEY must be set as an environment variable for security.")

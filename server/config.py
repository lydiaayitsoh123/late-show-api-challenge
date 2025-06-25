import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        'postgresql://lydia:okwemba@localhost:5432/late_show_db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    if not JWT_SECRET_KEY:
        raise ValueError("JWT_SECRET_KEY must be set as an environment variable for security.")

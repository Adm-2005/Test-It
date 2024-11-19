import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_DB_URI = os.getenv("DATABASE_URL", "mongodb://localhost:27017/defaultdb")
    JWT_SECRET = os.getenv("JWT_SECRET", "zdskaoisefoewqweorwejakldsfawoeiiq132416459844i3dzk")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 18000))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", 86400))
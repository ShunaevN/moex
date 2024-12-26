from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
KEY = os.environ.get("SECRET_KEY")
MODE = os.environ.get("MODE")
BASE_HISTORY_URL=os.environ.get("BASE_HISTORY_URL")
BASE_SECURITIES_URL=os.environ.get("BASE_SECURITIES_URL")

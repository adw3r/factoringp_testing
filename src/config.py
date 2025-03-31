import os
import pathlib

from dotenv import load_dotenv

load_dotenv()
ROOT_DIR = pathlib.Path(__file__).parent.parent


MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_PORT = os.environ['MYSQL_PORT']
DATABASE_URL = f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

APP_HOST = os.environ['APP_HOST']
APP_PORT = os.environ['APP_PORT']

SECRET = os.environ['SECRET']

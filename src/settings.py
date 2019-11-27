import os
from distutils.util import strtobool
from dotenv import load_dotenv


load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST", 'root')
MYSQL_PORT = os.getenv("MYSQL_PORT", 'root')
MYSQL_USER = os.getenv("MYSQL_USER", 'root')
MYSQL_PASS = os.getenv("MYSQL_PASS", 'root')

BACKUP_PATH = os.getenv("BACKUP_PATH", '.')

S3_ENABLED = strtobool(os.getenv("S3_ENABLED", 'False'))
S3_BUCKET = os.getenv("S3_BUCKET", '')
S3_PATH = os.getenv("S3_PATH", '')

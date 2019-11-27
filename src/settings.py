import os
from dotenv import load_dotenv


load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST", 'root')
MYSQL_PORT = os.getenv("MYSQL_PORT", 'root')
MYSQL_USER = os.getenv("MYSQL_USER", 'root')
MYSQL_PASS = os.getenv("MYSQL_PASS", 'root')
BACKUP_PATH = os.getenv("BACKUP_PATH", '.')

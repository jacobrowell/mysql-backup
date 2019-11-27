import os
from dotenv import load_dotenv


load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER", 'root')
MYSQL_PASS = os.getenv("MYSQL_PASS", 'root')
BACKUP_PATH = os.getenv("BACKUP_PATH", '.')

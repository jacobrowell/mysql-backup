#!/usr/bin/env python3
import logging
import os
import subprocess
import sys
from datetime import datetime

from sqlalchemy import create_engine

import settings


DB_BLACKLIST = ['mysql', 'phpmyadmin', 'information_schema', 'performance_schema']

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/?charset=utf8mb4".format(
    settings.MYSQL_USER,
    settings.MYSQL_PASS,
    settings.MYSQL_HOST,
    settings.MYSQL_PORT,
))

export_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

user = settings.MYSQL_USER
password = settings.MYSQL_PASS
backup_path = settings.BACKUP_PATH

if not os.path.isdir(backup_path):
    if os.path.exists(backup_path):
        logging.error("backup path exists and is not a directory")
        sys.exit(1)
    else:
        os.makedirs(backup_path, 0o755)

databases = engine.execute("SHOW DATABASES").fetchall()
databases = [db[0] for db in databases if db[0] not in DB_BLACKLIST]

for db_name in databases:
    export_file_name = f"{db_name}_{export_timestamp}.sql"
    command = f"mysqldump -u{user} -p{password} {db_name} > {backup_path}/{db_name}.sql &"
    subprocess.call(command, shell=True)

if settings.S3_ENABLED:
    command = f"aws s3 sync {backup_path} {settings.S3_BUCKET}{settings.S3_PATH}"
    subprocess.call(command, shell=True)

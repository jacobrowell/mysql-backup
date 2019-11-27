#!/usr/bin/python

import os
import subprocess
from config import config


user = config.get('user')
password = config.get('password')
backup_path = config.get('backup_dir')

if not os.path.exists(backup_path) or not os.path.isdir(backup_path):
    os.mkdir(backup_path, 0o755)

databasesRaw = subprocess.check_output("mysql -u{} -p{} -e 'show databases;'".format(user, password), shell=True)

databases = databasesRaw.split()
exclude_db = ['Database', 'mysql', 'phpmyadmin', 'information_schema', 'performance_schema']
databases = [db for db in databases if db not in exclude_db]

for dbName in databases:
    command = 'mysqldump -u{} -p{} {} > {}/{}.sql &'.format(user, password, dbName, backup_path, dbName)
    subprocess.call(command, shell=True)

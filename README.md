# sqlautoackup

Python script for dumping & optional backup of mysql databases

I made this script for my own custom scenario:
- dump local databases mysql databases
- sync dump files to a specific path in an s3 bucket using AWS CLI

## Prerequisites

- Python 3 (works on 3.6+, may also work on older versions)
- AWS CLI installed and configured (if you want to upload dumps to S3)

## Setup and usage

To set this up you need to:
1. Copy `src/.env.example` to `src/.env` and populate it with appropriate values
2. Install python dependencies using Pipenv: `cd src && pipenv install`

To run the script you should execute following command in `src` subdirectory:

```
pipenv run python sqlbackup.py
```

This will dump all local databases except "system" ones
(those are by default: 'information_schema', 'mysql', 'performance_schema', 'phpmyadmin', 'sys')
to a specified local `BACKUP_PATH` and then, if backup to S3 is enabled and configured
run `aws s3 sync` from local backup dir to a specified S3 bucket.

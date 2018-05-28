import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv


def set_env_path():
    # set the environment path
    env_path = Path('..') / '.env'
    load_dotenv(dotenv_path=env_path)


def aws_connect():
    # establish connection to AWS database instance
    host = "bikeshare-restored.cs9te7lm3pt2.us-east-1.rds.amazonaws.com"
    port = 5432
    database = "bikeshare"
    user = os.environ.get("AWS_READONLY_USER")
    password = os.environ.get("AWS_READONLY_PASS")
    conn = psycopg2.connect(host=host, user=user, port=port, password=password, database=database)
    cur = conn.cursor()
    return conn, cur
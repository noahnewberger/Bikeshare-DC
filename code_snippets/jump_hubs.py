import requests
from dotenv import load_dotenv
from pathlib import Path
import os


def set_env_path():
    # set the environment path
    env_path = Path('..') / '.env'
    load_dotenv(dotenv_path=env_path)


def jump_proxy():
    JUMP_URL = "https://app.socialbicycles.com/api/hubs"
    username = os.environ.get("JUMP_USER")
    password = os.environ.get("JUMP_PASS")
    resp = requests.get(JUMP_URL, auth=requests.auth.HTTPBasicAuth(username, password))
    return resp.json()


if __name__ == "__main__":
    set_env_path()
    jump_resp = jump_proxy()
    print(jump_resp)


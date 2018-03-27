import requests
import util_functions as uf
import os


def jump_proxy():
    JUMP_URL = "https://app.socialbicycles.com/api/hubs"
    username = os.environ.get("JUMP_USER")
    password = os.environ.get("JUMP_PASS")
    resp = requests.get(JUMP_URL, auth=requests.auth.HTTPBasicAuth(username, password))
    return resp.json()


if __name__ == "__main__":
    uf.set_env_path()
    jump_resp = jump_proxy()
    print(jump_resp)


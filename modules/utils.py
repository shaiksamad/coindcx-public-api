import time
import requests


def check_resp(resp: requests.models.Response, func=requests.models.Response.json):
    if resp.status_code == 200:
        return func(resp)
    # elif resp.status_code =
    return [resp.status_code]


def timestamp():
    return int(round(time.time() * 1000))

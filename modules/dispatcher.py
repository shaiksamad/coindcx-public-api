import hashlib
import hmac
import json
# import time
from errors import *

import requests

# from modules import user


class Dispatcher:
    def __init__(self, key, secret, body, url):
        __key, __secret = key, secret

        __body = json.dumps(body, separators=(",", ":"))

        __signature = hmac.new(bytes(__secret, encoding='utf-8'), __body.encode(), hashlib.sha256).hexdigest()

        __headers = {
            'Content-Type': 'application/json',
            'X-AUTH-APIKEY': __key,
            'X-AUTH-SIGNATURE': __signature
        }

        # try:
        response = requests.post(url, data=__body, headers=__headers)
        # except Exception as exp:
        #     print(exp)

        # message = response.json()['message'] if response.status_code != 200 is not None else None
        if response.status_code != 200 and response.content != b'':
            print(response.json())
            message = response.json()['message']
        else:
            message = None
        # message = response.content if response.status_code != 200 and response.content != b'' else None
        # print(response.content)

        errors = {
            400: BadRequestError,
            401: UnauthorizedError,
            404: NotFoundError,
            429: TooManyRequestsError,
            500: InternalServerError,
            503: ServiceUnavailableError
        }

        if response.status_code in errors:
            raise errors[response.status_code](message)

        self.resp = response
        self.data = response.json()


if __name__ == "__main__":
    # from modules.user import timestamp
    # key = "9d880b1490b24203413592a82136c9e255f87ed1872d20b3"
    # sec = "90269bb2c714400b4250fefefe250e72ec34b54c5cf76abebaa1d3596813dddb"
    # body = {
    #     "timestamp": timestamp()
    # }
    # url = 'https://api.coindcx.com/exchange/v1/users/info'
    # d = Dispatcher(key, sec, body, url)
    # print(d.data)
    # print(d.resp)

    while 1:
        try:
            print(eval(input(">>> ")))
        except Exception as e:
            print(e)

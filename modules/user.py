import time

from modules.dispatcher import Dispatcher
from modules.utils import timestamp


class User:
    def __init__(self, key, secret):
        self.baseurl = "https://api.coindcx.com/exchange/v1/users"
        self.key = key
        self.secret = secret

    def __get(self, q="balances"):
        d = Dispatcher(self.key, self.secret, {"timestamp": timestamp()}, self.baseurl+f'/{q}')
        if d.resp.status_code == 200:
            return d.data
        raise ConnectionError(d.resp)

    def balances(self, *currency: str) -> dict or list[dict]:
        currency = list(currency)
        balance = self.__get('balances')
        output = []
        [(output.append(bal), currency.remove(bal['currency'])) for bal in balance if bal['currency'] in currency]

        if currency:
            raise ValueError(f"{currency} invalid currency ")
        if output:
            return output if len(output) > 1 else output[0]
        return balance

    def info(self):
        return self.__get("info")


if __name__ == "__main__":
    # key = "9d880b1490b24203413592a82136c9e255f87ed1872d20b3"
    # sec = "90269bb2c714400b4250fefefe250e72ec34b54c5cf76abebaa1d3596813dddb"

    key = "972f72efdfb040d99eeba331cb1e6cbae671b77bc0710bdb"
    sec = "8b43647cb886e9c8d26272a535e6a5ba0055094c460675fd0e0fedd44d9eeb39"
    u = User(key, sec)
    bal = u.balances("USDT")
    print(u.balances())
    # print(u.info())
    while 1:
        try:
            inp = input(">>> ")
            start = time.time()
            print(eval(inp))
        except Exception as e:
            print(e)
        print(f"it took {time.time() - start} seconds")
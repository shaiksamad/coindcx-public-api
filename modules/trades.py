import requests
from modules.utils import check_resp


class Trades:
    def __init__(self):
        self.base_url = "https://public.coindcx.com/market_data/trade_history"

    def history(self, pair, exchange="B", limit="50") -> list:
        resp = requests.get(self.base_url, params={"pair": exchange + "-" + pair, "limit": limit})
        return check_resp(resp)

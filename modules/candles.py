import requests
from modules.utils import check_resp


class Candle:
    def __init__(self, open, high, low, volume, close, time):
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.time = time


class Candles:
    def __init__(self, pair, interval, start_time=None, end_time=None, limit=500, exchange="B"):
        __interval__ = {"1m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "1d", "3d", "1w", "1M"}
        __exchange__ = {"B", "I", "HB", "H", "BM"}
        self.pair = pair
        self.interval = interval if interval in __interval__ else "1m"
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit if limit in range(0, 1001) else 500
        self.exchange = exchange if exchange in __exchange__ else "B"
        self.baseurl = "https://public.coindcx.com/market_data/candles"
        self.params = {}
        self.set_params()

    def query(self):
        resp = requests.get(self.baseurl, params=self.params)
        resp = check_resp(resp)
        result = []
        if len(resp) > 1:
            for cand in resp:
                result.append(Candle(**cand))
        return result

    def set_params(self):
        self.params = {
            "pair": self.exchange+"-"+self.pair,
            "interval": self.interval,
            "startTime": self.start_time,
            "endTime": self.end_time,
            "limit": self.limit
        }


if __name__ == "__main__":
    params = {
        "pair": "BTC_USDT",
        "interval": "1m",
        "limit": 10
    }
    candles = Candles(**params)
    for cand in candles.query():
        print(cand.low, cand.high, cand.volume, cand.open, cand.close, sep=", ")
    # print(candles.query())

import requests
from time import time
# try:
from modules.utils import check_resp
from modules.candles import Candles
from modules.markets import Markets
from modules.ticker import Ticker
from modules.trades import Trades
# except ModuleNotFoundError:
    # from .utils import check_resp
    # from .candles import Candles
    # from .markets import Markets
    # from .ticker import Ticker
    # from .trades import Trades

class Public:
    def __init__(self):
        self.base_url = "https://api.coindcx.com/exchange"
        self.markets = Markets().list  # Markets().list()
        self.markets_details = Markets().details  # Markets().list()
        self.trades = Trades().history  # Trades
        # self.candles = self._candles

    def ticker(self, market: str = None):
        resp = requests.get(self.base_url + "/ticker")
        resp = check_resp(resp)
        if resp is not None:
            if market is not None and market.upper() in Markets().list():
                for tick in resp:
                    if tick['market'] == market.upper():
                        return Ticker(**tick)
        temp = []
        for tick in resp:
            temp.append(Ticker(**tick))
        return temp

    def candles(self, pair, interval, start_time=None, end_time=None, limit=500, exchange="B"):
        return Candles(pair, interval, start_time, end_time, limit, exchange).query()

    def order_book(self, pair: str, ecode="B"):
        resp = requests.get(f"https://public.coindcx.com/market_data/orderbook?pair={ecode}-{pair}")
        return resp.json()




if __name__ == "__main__":
    public = Public()
    start = time()
    print(start)
    # for i in range(100):
    #     candles = public.candles("BTC_USDT", "1m", limit=2)[0]
    #     for candle in candles:
    #         print(candle.close)
        # print(candles.close)
        # sleep(.95)
        # print()
    print(time()-start)
    avg = []
    while 1:
        try:
            inp = input(">>> ")
            start = time()
            # output = eval(inp)
            # print(output) if output else None
            print(eval(inp))
        except Exception as e:
            print(e)
        end = time()-start
        avg.append(end) if inp.__contains__(" in ") else None
        print(f"It took \"{end}\" seconds for your query")

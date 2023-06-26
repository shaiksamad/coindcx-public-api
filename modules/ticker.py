

class Ticker:
    def __init__(self, **kwargs):
        self.market = self.change_24_hour = self.high = self.low = self.volume = self.last_price = self.ask = self.bid \
            = self.timestamp = None

        __attr__ = ["market", "change_24_hour", "high", "low", "volume", "last_price", "bid", "ask", "timestamp"]

        self.__dict__.update((item, value) for item, value in kwargs.items() if item in __attr__)

    def __str__(self):
        return str(self.__dict__)

    def json(self):
        return self.__dict__

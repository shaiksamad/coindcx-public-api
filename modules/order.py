import time

import requests

from modules.dispatcher import Dispatcher
from modules.public import Public, Markets
from modules.utils import timestamp
from modules.user import User


class CreateOrder:
    def __init__(self, side: str,
                 market: str,
                 total_quantity: int,
                 price_per_unit: int = None,
                 ecode: str = None):
        self.side = side  # buy, sell
        self.market = market  # USDTINR
        self.total_quantity = total_quantity
        self.price_per_unit = price_per_unit if price_per_unit is not None else ""
        self.order_type = 'limit order' if price_per_unit is not None else 'market_order'
        self.timestamp = timestamp()  # 1524211224
        # if ecode != "":
        self.ecode = ecode if ecode is not None else "I"  # I, B, HB

    def body(self):
        return self.__dict__


class OrderResponse:
    __slots__ = ['id', 'market', 'order_type', 'side', 'status', 'fee_amount', 'fee', 'total_quantity',
                 'remaining_quantity', 'avg_price', 'price_per_unit', 'created_at', 'updated_at']

    def __init__(self, **kwargs):
        [self.__setattr__(i, v) for i, v in kwargs.items() if i in self.__slots__]

    def body(self):
        return self.__dict__


class Orders:
    def __init__(self, user: User = None, key=None, secret=None):
        if user is not None:
            self.key = user.key
            self.secret = user.secret
        else:
            self.key = key
            self.secret = secret
        self.baseurl = "https://api.coindcx.com/exchange/v1/orders"

    @staticmethod
    def __validate(order: CreateOrder):
        if order.side not in ("buy", "sell"):
            raise ValueError("side must be 'buy' or 'sell'")
        if order.market not in Markets().list():
            raise ValueError(f"{order.market} is not a valid market")
        market = Markets().details(order.market)
        if not (market.min_quantity <= order.total_quantity <= market.max_quantity):
            raise ValueError(f"total_quantity of {order.market} must be in between {market.min_quantity} to "
                             f"{market.max_quantity}")
        if order.order_type == 'limit_order':
            if (order.price_per_unit * order.total_quantity) < market.min_notional:
                raise ValueError(f"minimum order value must be {market.min_quantity} {market.base_currency_short_name}")
            if not (market.min_price <= order.price_per_unit <= market.max_price):
                raise ValueError(f"price_per_unit must be in between {market.min_price} to {market.max_price}")
        if 'ecode' in order.body() and order.ecode not in ("I", "B", "HB"):
            raise ValueError("ecode must be I, B or HB")

    def new(self, orders: CreateOrder or list[CreateOrder]):
        if type(orders) == list:
            for order in orders:
                self.__validate(order)
            del order
            body = {
                'orders': [order.body() for order in orders]
            }
            return Dispatcher(self.key, self.secret, body, self.baseurl + '/create_multiple').data

        self.__validate(orders)
        return Dispatcher(self.key, self.secret, orders.body(), self.baseurl + '/create').data

    def status(self, order_ids: str or list[str]) -> dict or list[dict]:
        if type(order_ids) is str:
            return Dispatcher(self.key, self.secret, {'id': order_ids, 'timestamp': timestamp()},
                              self.baseurl + '/status').data
        return Dispatcher(self.key, self.secret, {'ids': order_ids, 'timestamp': timestamp()},
                          self.baseurl + '/status_multiple').data

    def history(self):
        return Dispatcher(self.key, self.secret, {'timestamp': timestamp()}, self.baseurl + '/trade_hhistory').data

    def cancel_all(self, market: str, side: str = None):
        return Dispatcher(self.key, self.secret,
                          {"market": market, side: side if side else "", "timestamp": timestamp()},
                          self.baseurl + '/cancel_all').data


if __name__ == "__main__":
    # o = Order("buy", "market_order", "open", 1234567890, "I")
    key = "9d880b1490b24203413592a82136c9e255f87ed1872d20b3"
    sec = "90269bb2c714400b4250fefefe250e72ec34b54c5cf76abebaa1d3596813dddb"
    u = User(key, sec)
    o = Orders(key=key, secret=sec)
    balances = u.balances()
    for balance in balances:
        if balance['balance'] != '0.0':
            print(balance)
    # orders = [
    #     CreateOrder('buy', 'USDTINR', 2, 75),
    #     CreateOrder('buy', 'USDTINR', 2, 75)
    # ]
    # order = o.new(orders[0])
    # order = o.new([*orders])

    # while 1:
    #     print(Dispatcher(key, sec, {"timestamp": timestamp()}, 'https://api.coindcx.com/exchange/v1/users/balances').data)

    # print(order)
    print(o.history())

    # single = o.status('abe074d78-4cf8-11ec-8e8a-a34359d413b0')
    # multi = o.status(["be074d78-4cf8-11ec-8e8a-a34359d413b0", "2b3ded48-4b7d-11ec-ae70-03c52b672ba4"])
    # print(1, o.status("sbe074d78-4cf8-11ec-8e8a-a34359d413b0"))
    # print(2, o.status(["be074d78-4cf8-11ec-8e8a-a34359d413b0", "2b3ded48-4b7d-11ec-ae70-03c52b672ba4"]))
    # 2b3ded48-4b7d-11ec-ae70-03c52b672ba4
    # be074d78-4cf8-11ec-8e8a-a34359d413b0
    # print(id(o))
    # print(o1.new('buy', 'USDTINR', 10, 70, 'limit_order'))
    # print(o.history())
    # h = o.history()
    # print(h)
    # print(single, multi, sep="\n")

    # print(o.side)

    while 1:
        try:
            inp = input(">>> ")
            start = time.time()
            print(eval(inp))
        except Exception as e:
            print(e)
        print(f"it took {time.time() - start} seconds")

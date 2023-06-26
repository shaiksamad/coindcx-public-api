from time import time
# import sys

import requests
from modules.utils import check_resp


class Details:
    __slots__ = ['coindcx_name', 'base_currency_short_name', 'target_currency_short_name', 'target_currency_name',
                 'base_currency_name', 'min_quantity', 'max_quantity', 'max_quantity_market', 'min_price', 'max_price',
                 'min_notional', 'base_currency_precision', 'target_currency_precision', 'step', 'order_types',
                 'symbol', 'ecode', 'max_leverage', 'max_leverage_short', 'pair', 'status']

    def __init__(self, **kwargs):
        [self.__setattr__(i, v) for i, v in kwargs.items() if i in self.__slots__]


class Markets:
    def __init__(self):
        super(Markets, self).__init__()
        self.base_url = 'https://api.coindcx.com/exchange/v1/markets'
        # self.base_url += '/v1/markets'

    def list(self) -> list:
        resp = requests.get(self.base_url)
        return check_resp(resp)

    def details(self, market: str = None) -> Details or list[Details]:  # get details of market ex: USDTINR
        resp = requests.get(self.base_url + '_details')
        resp = check_resp(resp)
        if len(resp) > 1:
            if market is not None:
                for mark in resp:
                    if mark['coindcx_name'] == market:
                        return Details(**mark)
        data = []
        for detail in resp:
            data.append(Details(**detail))
        return data


#
if __name__ == "__main__":
    m = Markets()
    # print(m.details())
    a = {'coindcx_name': 'USDTINR', 'base_currency_short_name': 'INR', 'target_currency_short_name': 'USDT',
         'target_currency_name': 'Tether', 'base_currency_name': 'Indian Rupee', 'min_quantity': 0.01,
         'max_quantity': 100000.0, 'max_quantity_market': 10000000.0, 'min_price': 26.52333333333333, 'max_price':
             238.71, 'min_notional': 100.0, 'base_currency_precision': 2, 'target_currency_precision': 2, 'step': 0.01,
         'order_types': ['limit_order'], 'symbol': 'USDTINR', 'ecode': 'I', 'max_leverage': None,
         'max_leverage_short': None, 'pair': 'I-USDT_INR', 'status': 'active'}

    details = Details(**a)

    while 1:
        try:
            inp = input(">>> ")
            start = time()
            # output = eval(inp)
            # print(output) if output else None
            print(eval(inp))
        except Exception as e:
            print(e)
        end = time() - start
        # avg.append(end) if inp.__contains__(" in ") else None
        print(f"It took \"{end}\" seconds for your query")

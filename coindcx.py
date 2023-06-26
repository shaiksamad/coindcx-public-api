from modules.public import Public

public = Public()

ticker = public.ticker
markets = public.markets
markets_details = public.markets_details
trades = public.trades
order_book = public.order_book
candles = public.candles

print(order_book("BTC_USDT"))


if __name__ == "__main__":
    pass

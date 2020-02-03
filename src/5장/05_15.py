import pybithumb

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']
print(close)

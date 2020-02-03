import pybithumb

df = pybithumb.get_ohlcv('BTC')
ma5 = df['close'].rolling(window=5).mean()
last_ma5 = ma5[-2]

price = pybithumb.get_current_price('BTC')

if price > last_ma5:
    print('상승장')
else:
    print('사락장')
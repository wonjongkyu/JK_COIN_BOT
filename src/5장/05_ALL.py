import pybithumb
import time
import datetime

# 5.1.2 가상화폐 티커 목록 얻기
tickers = pybithumb.get_tickers()
print(tickers)
print(len(tickers))     # tickers의 length

# 5.1.3 현재가 얻기
price = pybithumb.get_current_price("BTC","KRW")    # 뒤에 기축 KRW는 생략 가능함
print(price)

# 2초에 한 번씩 시세 가져오기
"""
while True:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(2)
"""

# 빗썸에 모든 코인 현재가격 가져오기
"""
tickers = pybithumb.get_tickers()
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(price)
    time.sleep(0.1)
"""

# 5.1.4 거래소 거래 정보 (시가, 고가, 저가, 종가, 거래량)
detail = pybithumb.get_market_detail("BTC")
print(detail)

# 5.1.5 호가
print("orderbook==============================")
orderbook = pybithumb.get_orderbook("BTC", 'KRW', 20)
print(orderbook)

for k in orderbook:
    print(orderbook[k])

print('ordertimestampd::' + orderbook['timestamp'])
ms = int(orderbook['timestamp'])

df = datetime.datetime.fromtimestamp(ms/1000)
print(df)

# 매수/매도 호가 접근하기
print("매수/매도 호가 접근하기")
bids = orderbook['bids']
asks = orderbook['asks']
print(bids)
print(asks)

for bid in bids:
    print(bid)

# 매수호가 출력하기
bids = orderbook['bids']

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print("매수호가:", price, "매수잔량:", quant)

# 매도호가 출력하기
print("------------------------------------매도호가 출력하기---------------------------------")
asks = orderbook['asks']

for ask in asks:
    price = ask['price']
    quant = ask['quantity']
    print("매도호가:", price, "매도잔량:", quant)

# 5.1.6 여러 가상화폐에 대한 정보 한번에 얻기
all = pybithumb.get_current_price("ALL")
for k, v in all.items():
    print(k, v)

# 모든 가상화폐에 대한 현재가 가져오기
all = pybithumb.get_current_price("ALL")
for ticker, data in all.items():
    print(ticker, data['closing_price'])


# 5.1.7 예외처리
price = {'open': 100, 'high': 150, 'low': 90, 'close': 130}
print("point-1")

try:
    open = price['open1']
except:
    pass
print("point-2")
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" 2.2.1 for문 """
for value in ["가", "나", "다", "라"]:
    print(value) 
    
ripple = [511, 516, 508, 505, 503]
for close in ripple:
    print(close)
    
for 좌석 in ["좌석1", "좌석2", "좌석3", "좌석4", "좌석5", "좌석6"]:
    print(좌석, "표 확인")

tickers = ["BTC", "BTG", "BCH", "XRP", "ETH", "DASH"]
for ticker in tickers:
    print(ticker)
    
    
""" 2.2.2. for와 range """
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)
print()

for num in range(1, 11):
    print(num)
print()

for num in range(1, 11, 3): 
    print(num)
print()

    
""" 2.2.3 for와 딕셔너리 """
cur_price = {"BTC": 9010000, "XRP": 511, "DASH": 360000}
for ticker in cur_price:
    print(ticker)
print()
    
for ticker, price in cur_price.items():
    print(ticker, price)
print()

for ticker in cur_price:
    print(ticker, cur_price[ticker])
    
""" 2.2.4 반복문과 if """
ripple = [511, 516, 508, 505, 503]
for close in ripple:
    if close >= 510:
        print(close)
print()


""" 2.2.5 while 문 """
num = 1
while True:
    if num == 100 :
        break
    print(num)
    num = num + 1
    
""" 2.2.6 연습 문제 """
for num in range(10, 21):
    print(num)

for year in range(2002, 2051, 4):
    print(year)

portfolio = ["BTC_KRW", "BCH_KRW", "XRP_KRW", "DASH_KRW", "LTC_KRW"]
for ticker in portfolio:
    print(ticker[-4:])


    
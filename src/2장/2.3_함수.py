# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:11:40 2020

@author: jongkyu
"""

""" 2.3.1 파이썬 함수 정의하기 """
def hap(a, b):
    ret = a+ b
    return ret

result = hap(3, 4)
print(result)
print()

result1 = hap(5, 6)
print(result1)
result2 = hap(10, 20)
print(result2)

def print_ohlc(open, high, low, close):
    print("시가: ", open)
    print("고가: ", high)
    print("저가: ", low)
    print("종가: ", close)

print_ohlc(100, 120, 80, 90)
print()

#print_ohlc(100, 120, 80)
 
def print_ohlc2(ohlc):
    print("시가: ", ohlc[0])
    print("고가: ", ohlc[1])
    print("저가: ", ohlc[2])
    print("종가: ", ohlc[3])
xrp_ohlc = [100, 120, 80, 90]
print_ohlc2(xrp_ohlc)
print()

def get_min_order(ticker):
    min_order = None
    if ticker == "ETC":
        min_order = 0.1
    elif ticker == "ETH":
        min_order = 0.5
    elif ticker == "BTC":
        min_order = 0.01
    elif ticker == "XRP":
        min_order = 10
    else:
        min_order = 0.005
    return min_order

min_order = get_min_order("BTC")
print(min_order)
print()

min_order = get_min_order("XRP")
print(min_order)
print()

""" 2.3.2 함수는 이름표 """
print("*" * 40)
print("*" * 80)

def 별찍기():
    print("*" * 40)
    print("*" * 80)

별찍기()

""" 2.3.3 함수 호출 이해하기 """
def mysum(a, b):
    ret = a + b
    return ret

ret = mysum(3, 4)
print(ret)
print()

""" 2.3.4 연습 문제 """
def mygob(a, b):
    ret = a * b
    return ret
print()

def convert_ticker(ticker):
    ret = ticker.upper()
    return ret
ret = convert_ticker('btc')
print(ret)
print()

def pickup_event(numbers):
    ret = []
    for num in numbers:
        if num % 2 == 0:
            ret.append(num)
    return ret

ret = pickup_event([1,2,3,4,5,6,7,8,9])
print(ret)












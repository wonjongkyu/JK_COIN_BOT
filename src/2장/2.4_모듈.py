# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:17:03 2020

@author: jongkyu
"""

""" 2.4.2 모듈 만들기 """


""" 2.4.3 모듈을 import 하는 방법 """
"""
    import 모듈
    ex) import coin
        coin.get_open_price('BTC')
        
    import 모듈 as 새이름
    ex) import coin as newname
        newname.get_open_price('BTC)
        
    from 모듈 import 함수
    ex) from coin import get_open_price
        get_open_price()
    ex) from coin import get_open_price, get_close_price
        
    from 모듈 import *
    ex) from coin import *

""" 
from coin import get_open_price
get_open_price('BTC')


""" 2.4.4 datetime 모듈 """
import datetime
now = datetime.datetime.now()
print(now)
print(now + datetime.timedelta(hours=10))
print(now + datetime.timedelta(minutes=30))


""" 2.4.5 requests 모듈 """
import requests
resp = requests.get("https://api.bithumb.com/public/ticker/BTC")
print(resp)
print(resp.content)


""" 2.4.6 연습 문제 """
print(now + datetime.timedelta(hours=5) + datetime.timedelta(minutes=30))
print(now - datetime.timedelta(days=3))
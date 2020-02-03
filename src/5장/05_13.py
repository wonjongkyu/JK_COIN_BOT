import pybithumb
import time

# if문을 통한 예외처리
while True:
    price = pybithumb.get_current_price("BTC")
    if price is not None:
        print(price/10)
    time.sleep(0.2)


# try - except 구문을 이용한 예외처리
while True:
    price = pybithumb.get_current_price("BTC")
    try:
        print(price / 10)
    except:
        print("에러 발생", price)
    time.sleep(0.2)


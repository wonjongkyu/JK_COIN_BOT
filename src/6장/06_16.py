import time
import datetime
import pybithumb

def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]  # 끝에서 두 번쨰 행(전일 데이터)를 가져옵니다.

    today_open = yesterday['close']  # 전일 종가
    yesterday_high = yesterday['high']  # 전일 고가
    yesterday_low = yesterday['low']  # 전일 저가
    target = today_open + (yesterday_high + yesterday_low) * 0.5
    return target

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
get_target_price("BTC")

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.timedelta(seconds=10) :
        target_price = get_target_price("BTC")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
    current_price = pybithumb.get_current_price("BTC")
    print(current_price)

    time.sleep(1)
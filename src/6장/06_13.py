import pybithumb

df = pybithumb.get_ohlcv("BTC")
yesterday = df.iloc[-2]         # 끝에서 두 번쨰 행(전일 데이터)를 가져옵니다.

today_open = yesterday['close']         # 전일 종가
yesterday_high = yesterday['high']      # 전일 고가
yesterday_low = yesterday['low']        # 전일 저가
target = today_open + (yesterday_high + yesterday_low) * 0.5
print(target)                           # 레리 윌리엄스 변동성 돌파 전략의 목표가를 계산한다.
import requests

#r = requests.get("https://api.upbit.com/v1/ticker?markets=KRW-BTC")
r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitcoin = r.json()
print(bitcoin)
print(bitcoin['last'])
print(bitcoin['bid'])
print(bitcoin['ask'])
print(bitcoin['volume'])
print(type(bitcoin))

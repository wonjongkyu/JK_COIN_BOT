# 4.2.1 HTML 문서 다운로드 및 파싱
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_per")
tag = tags[0]
print(tag.text)
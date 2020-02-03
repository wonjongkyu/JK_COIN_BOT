# 5.4.2 스레드 적용하기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb
import time

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("../../Qt_Designer/bull.ui")[0]

class Worker(QThread):
    def run(self):
        while True:
            data = {}


            for ticker in tickers:
                data[ticker] = self.get_market_infos(ticker)

            print(data)
            time.sleep(5)

    def get_market_infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            ma5 = df['close'].rolling(window=5).mean()
            last_ma5 = ma5[-2]
            price = pybithumb.get_current_price(ticker)

            state = None
            if price > last_ma5:
                state = '상승장'
            else:
                state = '하락장'

            return price, last_ma5, state
        except:
            return None, None, None


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()

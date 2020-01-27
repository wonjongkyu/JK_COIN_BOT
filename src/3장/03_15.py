# https://www.iconfinder.com/
# http://www.myiconfinder.com/

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 400)    # 좌측 상단으로 부터 (x,y) 거리  / 창 크기 (x,y)
        self.setWindowTitle('PyQt')             # Title
        self.setWindowIcon(QIcon("icon.png"))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

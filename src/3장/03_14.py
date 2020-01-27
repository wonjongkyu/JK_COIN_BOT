import sys
from idlelib import window

from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        #parent = super()
        #parent.__init__()


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
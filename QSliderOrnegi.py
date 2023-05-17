from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):





        self.setWindowTitle("QSlider örneği")
        self.show()
if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
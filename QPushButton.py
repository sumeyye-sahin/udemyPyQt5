from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.giris=QLineEdit()
        button=QPushButton("yaziyi yazdır")

        v_box=QVBoxLayout()
        v_box.addWidget(self.giris)
        v_box.addWidget(button)
        self.setLayout(v_box)
        button.clicked.connect(self.yap)
        self.show()
    def yap(self):
        self.setWindowTitle(self.giris.text())

if __name__=="__main__":
    app=QApplication(sys.argv)

    pencere =Pencere()
    sys.exit(app.exec())
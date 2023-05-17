from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.label=QLabel()
        button1=QPushButton("buton 1")
        button2=QPushButton("buton 2")
        button3=QPushButton("buton 3")

        v_box=QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(button1)
        v_box.addWidget(button2)
        v_box.addWidget(button3)

        self.setLayout(v_box)
        button1.clicked.connect(lambda :self.yap(button1))
        button2.clicked.connect(lambda :self.yap(button2))
        button3.clicked.connect(lambda :self.yap(button3))
        self.show()
    def yap(self,e):
        self.label.setText(e.text())

if __name__=="__main__":
    app=QApplication(sys.argv)

    pencere =Pencere()
    sys.exit(app.exec())
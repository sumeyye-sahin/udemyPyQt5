from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):

        self.r1=QRadioButton("Mavi")
        self.r2=QRadioButton("Kırmızı")
        self.r3=QRadioButton("Yeşil")
        self.r4=QRadioButton("Sarı")

        self.grup1=QButtonGroup()
        self.grup2=QButtonGroup()

        self.grup1.addButton(self.r1)
        self.grup1.addButton(self.r2)

        self.grup2.addButton(self.r3)
        self.grup2.addButton(self.r4)

        h_box=QHBoxLayout()
        h_box.addWidget(self.r1)
        h_box.addWidget(self.r2)
        h_box.addWidget(self.r3)
        h_box.addWidget(self.r4)

        self.setLayout(h_box)

        self.show()



if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
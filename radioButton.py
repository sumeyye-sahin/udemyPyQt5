from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.r1=QRadioButton("Kadın")
        self.r2=QRadioButton("Erkek")

        h_box=QHBoxLayout()
        h_box.addWidget(self.r1)
        h_box.addWidget(self.r2)

        self.setLayout(h_box)


        self.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())

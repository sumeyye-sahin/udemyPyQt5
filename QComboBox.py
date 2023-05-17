from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.comB=QComboBox()
        self.comB.addItem("matematik")
        self.comB.addItem("türkçe")
        self.comB.addItem("fizik")
        self.comB.addItems(["kimya","tarih","coğrafya"])

        h_box=QHBoxLayout()
        h_box.addWidget(self.comB)
        self.setLayout(h_box)


        self.setWindowTitle("QComboBox")
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
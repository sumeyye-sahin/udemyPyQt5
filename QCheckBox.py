from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def yap(self):
        if self.cb.isChecked():
            print("Anlaşma kabul edilmiş !")
        else: print("Anlaşma kabul edilmemiştir !")
    def setUI(self):
        self.cb=QCheckBox("Anlaşmayı okuudm ve kabul ediyorum.")
        button=QPushButton("Gönder !")
        h_box=QHBoxLayout()
        h_box.addWidget(self.cb)
        h_box.addWidget(button)
        button.clicked.connect(self.yap)
        self.setLayout(h_box)
        self.setWindowTitle("QCheckBox")
        self.show()

if __name__=="__main__":
       app = QApplication(sys.argv)
       pencere = Pencere()
       sys.exit(app.exec())

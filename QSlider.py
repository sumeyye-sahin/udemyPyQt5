from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.s1=QSlider(Qt.Horizontal)
        #çubuğu yatauy hale getirmek için yazacağımız fonksiyon: s1=QSlider(Qt.Horizontal)  içine Qt.Horizontal yazmamız ile sağlanmış oldu
        #slider a tik ekleme
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setMinimum(0)
        self.s1.setMaximum(100)
        self.s1.setSingleStep(5)

        self.s1.valueChanged.connect(self.uygula)

        self.label1=QLabel("DEĞER: ")
        self.label2=QLabel()

        h_box=QHBoxLayout()
        h_box.addWidget(self.label1)
        h_box.addWidget(self.label2)



        v_box=QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.s1)
        self.setLayout(v_box)
        self.setWindowTitle("QSlider")
        self.show()

    def uygula(self):
        self.label2.setText(str(self.s1.value()))

if __name__=="__main__":
    app=QApplication(sys.argv)
    pancere=Pencere()
    sys.exit(app.exec())
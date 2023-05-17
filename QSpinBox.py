from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

#spine box=artırım ve azaltmalı line
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):

        #self.sb=QSpinBox()  # QDoubleSpinBox double değerler için bu fonksiyon çağrılır
        self.sb=QDoubleSpinBox()
        # self.sb.setMinimum(200)
        #self.sb.setMaximum(1000)
        #aynı değerleri şu şekilde de verebilirdik: self.sb.setRange(200,1000)
        self.sb.setRange(200,1000)
        self.sb.setSingleStep(20.5)
        self.sb.setValue(350) #başlangıç degeri atamak için yapılmış işlem
        self.sb.valueChanged.connect(self.uygula)

        v_box=QVBoxLayout()
        v_box.addWidget(self.sb)
        self.setLayout(v_box)

        self.setWindowTitle("QSpinBox")
        self.show()
    def uygula(self):
        print("Şuanki değer: {}".format(str(self.sb.value())))
        #girilen değer üzerinden işlem yapmak istersek bu şekilde değeri çekebiliyoruz.

if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
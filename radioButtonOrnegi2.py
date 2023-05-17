from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
#toplama çıkarma bölme çarpma örneği

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def hesapla(self):
        if self.r1.isChecked():
            sayi1=int(self.line.text())
            sayi2=int(self.line2.text())
            toplam=sayi1+sayi2
            self.label.setText(str(toplam))
        elif self.r2.isChecked():
            sayi1 = int(self.line.text())
            sayi2 = int(self.line2.text())
            toplam = sayi1 - sayi2
            self.label.setText(str(toplam))
        elif self.r3.isChecked():
            sayi1 = int(self.line.text())
            sayi2 = int(self.line2.text())
            toplam = sayi1 * sayi2
            self.label.setText(str(toplam))
        elif self.r4.isChecked():
            sayi1 = int(self.line.text())
            sayi2 = int(self.line2.text())
            toplam = sayi1 / sayi2
            self.label.setText(str(toplam))


    def setUI(self):

        button=QPushButton("HESAPLA")
        button.clicked.connect(self.hesapla)

        self.line=QLineEdit()
        self.line2=QLineEdit()
        self.label=QLabel("")
        self.r1=QRadioButton("TOPLAMA")
        self.r2=QRadioButton("ÇIKARMA")
        self.r3=QRadioButton("ÇARPMA")
        self.r4=QRadioButton("BÖLME")


        form=QFormLayout()
        form.addRow("Birinci Sayıyı Giriniz: ",self.line)
        form.addRow("İkinci Sayıyı Giriniz: ",self.line2)


        v_box=QHBoxLayout()

        v_box.addWidget(self.r1)
        v_box.addWidget(self.r2)
        v_box.addWidget(self.r3)
        v_box.addWidget(self.r4)


        form.addRow(v_box)
        form.addRow(self.label)
        form.addRow(button)

        self.setLayout(form)


        self.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
#açılır seçenek kutusu oluşturma
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.cb=QComboBox()
        self.chb=QCheckBox("Kabul ediyorum!")
        self.pb=QPushButton("Gönder")
        self.pb.clicked.connect(self.yasHesapla)
        self.cb.addItems(self.yillariOlusturma())
        #addItem bir item eklemyi sağlarken setItems ile birden fazla ityem ekleyebiliriz
        #addItems(["a","b","c"]) şeklinde dizi de gönderilebilir.
        h_box=QHBoxLayout()
        h_box.addWidget(self.cb)
        h_box.addWidget(self.chb)
        h_box.addWidget(self.pb)

        self.setLayout(h_box)

        self.show()
        self.setWindowTitle("QComboBox Örneği")

    def yillariOlusturma(self):
        liste=[str(x) for x in range(1960,2023)]
        return liste
    def yasHesapla(self):
        simdikiYil=2022
        kullanicininDT=int(self.cb.currentText())
        kYasi=simdikiYil-kullanicininDT
        print("Yaşınız: {}".format(kYasi))

if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
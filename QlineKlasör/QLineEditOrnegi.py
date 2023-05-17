from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

def pencere():

    def yap():
        kulAdi="Sümeyye"
        kulSifre=123456

        if kulAdi== isimGiris.text() and kulSifre==int(sifre.text()):
            girisDurumu.setText("HOŞGELDİNİZ!")

        else:
            isimGiris.clear()
            sifre.clear()
            girisDurumu.setText("Hatalı giriş tekrar deneyin!")

    app=QApplication(sys.argv)
    win=QWidget()
    win.setWindowTitle("QLineEditOrneği")
    isimGiris=QLineEdit()
    sifre=QLineEdit()
    sifre.setEchoMode(QLineEdit.Password)

    buton=QPushButton("GİRİŞ")
    buton.clicked.connect(yap)

    girisDurumu=QLabel("")

    form=QFormLayout()
    form.addRow("Kullanıcı adınızı giriniz: ",isimGiris)
    form.addRow("Şifreniizigiriniz: ",sifre)
    form.addRow(buton)
    form.addRow(girisDurumu)

    win.setLayout(form)

    win.show()
    sys.exit(app.exec())

if __name__=="__main__":
    pencere()
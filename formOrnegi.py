from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    app=QApplication(sys.argv)
    win=QWidget()
    win.setWindowTitle("Form Örneği")

    form=QFormLayout()
    form.addRow(QLabel("Kullanıcı Adı:"),QLineEdit())
    sifre=QLineEdit()
    sifre.setEchoMode(QLineEdit.Password)
    form.addRow(QLabel("Şifre:"),QLineEdit(sifre))
    form.addRow(QLabel("Adres:"), QTextEdit())


    lb1=QLabel("Şifre kayıt edilsin mi?")
    rb1=QRadioButton("Evet")
    rb2=QRadioButton("Hayır")

    h_box=QHBoxLayout()
    h_box.addWidget(rb1)
    h_box.addWidget(rb2)
    form.addRow(lb1,h_box)

    form.addRow(QPushButton("Gönder"),QPushButton("İptal et"))

    win.setLayout(form)


    win.show()
    sys.exit(app.exec())



if  __name__ == "__main__" :
      pencere()
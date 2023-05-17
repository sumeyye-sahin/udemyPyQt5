from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    app=QApplication(sys.argv)
    win=QWidget()
    win.setWindowTitle("Form")

    form=QFormLayout()
    form.addRow(QLabel("Adınız: "),QLineEdit())

    lb1=QLabel("Cinsiyet: ")
    rb1=QRadioButton("Kadın")
    rb2=QRadioButton("Erkek")

    h_box=QHBoxLayout()
    h_box.addWidget(rb1)
    h_box.addStretch()
    h_box.addWidget(rb2)

    form.addRow(lb1,h_box)
    form.addRow(QPushButton("Gönder"))

    win.setLayout(form)
    win.show()


    sys.exit(app.exec())

if __name__=="__main__":
    pencere()

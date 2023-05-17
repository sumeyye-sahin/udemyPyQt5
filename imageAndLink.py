from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

def window():
    app=QApplication(sys.argv)

    win=QWidget()
    win.setWindowTitle("on PyQt5: link , image")
   # label=QLabel("pencerede gözükmesini istediğimiz değer") #QLabel içine pencere ismi de yazılabilirdi , fakat ikisi birlikte yazılamaz

    label=QLabel()
    label2=QLabel()
    v_box=QVBoxLayout()

    # link yapısını html kodları sayesinde yapıyoruz
    label.setText("<a href=\"www.google.com\">Google'a git</a><br><i>Sümeyye Bilgisayar</b>")
    label.setOpenExternalLinks(True)
    gir

    #resim ekleme yöntemleri:
    label2.setPixmap(QPixmap("defneYapragi3D.jpg"))


    v_box.addWidget(label)
    v_box.addWidget(label2)
    win.setLayout(v_box)

    #labeli pencerenin ortaısna sabitlemek için: label.setAlignment(Qt.AlignCenter)
    label.setAlignment(Qt.AlignCenter)

    #labelin yazı tipini değiştirmrk için: label.setFont(QFont("Arial",17))
    label.setFont(QFont("Arial",17,QFont.Bold))



    win.show()

    sys.exit(app.exec())

if __name__=="__main__":
    window()
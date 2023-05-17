from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

#QLineEdit yazı yazma alnaı oluşturma için kullanılan fonksiyondur
#QTextEdit daha büyük metinlerin girişini yapmak için kullanılır
def pencere():

    def yap():
        print(giris.text())
        #girilen harfleri tek tek consola yazdırmak için oluşturulmuş fonksiyon:   giris.textChanged.connect(yap) ile çağrıldı

    app=QApplication(sys.argv)
    win=QWidget()
    win.setWindowTitle("QLine edit/ QText edit")

    giris2=QTextEdit()
    giris=QLineEdit()

    giris.textChanged.connect(yap)
    #yazı alanını sadece okunabilir yapmak için:
   # giris.setReadOnly(True)
    giris.setText("Sümeyye Şahin")

    #giriş alanına kendimize özel ayarlamak için: set inputMask ile örn: telefon nosu alınacak
    #giris.setInputMask("999_999_9999")

    #şifre girme alanı oluşturmak
    giris.setEchoMode(QLineEdit.Password)

    v_box=QVBoxLayout()
    v_box.addWidget(giris)
    v_box.addWidget(giris2)
    win.setLayout(v_box)

    win.show()


    sys.exit(app.exec())

if __name__=="__main__":
    pencere()

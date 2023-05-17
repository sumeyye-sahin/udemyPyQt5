0from PyQt5.QtCore import *
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        #self.showFullScreen() ile programı tam ekran yapabiliriz

       #arka planı renklendirme
        self.setAutoFillBackground(True) #arka planın renginin değişip değişemeyeceğine izin verme
        self.p=self.palette() #renk paleti sağlamış oluyor bu fonksiyon
        self.p.setColor(self.backgroundRole(),Qt.red)
        self.setPalette(self.p)
       #arka plan renk değiştirme buraya kadar yapılan kod satırlarıdır.


       # ses ekleme  kütüphane eklememiz gerekti pyqt.QtMultimedia
        self.media=QMediaPlayer()
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/sumeyye/Downloads/Manga-Yad-Eller.mp3")))

        self.sp=QSpinBox()
        self.sp.setRange(1,100)

        pb=QPushButton("Şarkıyı Çal!")
        pb2=QPushButton("Şarkıyı Duraklat!")
        pb3=QPushButton("Şarkıyı Kapat!")

        v_box=QVBoxLayout()
        v_box.addWidget(pb)
        v_box.addWidget(self.sp)
        v_box.addWidget(pb2)
        v_box.addWidget(pb3)

        self.sp.valueChanged.connect(self.sesDegistir)
        pb.clicked.connect(self.media.play)
        pb2.clicked.connect(self.media.pause)
        pb3.clicked.connect(self.close)


        self.setLayout(v_box)
        self.setGeometry(500,100,200,200)
        self.setWindowTitle("Kapsamlı Tasarım , Ses ekleme ,Arka plan renk değiştirme")
        self.show()
    def sarkiyiDuraklat(self):
        self.media.pause()

    def sarkiyiBaslat(self):

        self.sp.setValue(10)
        self.media.play()

    def sesDegistir(self):
        self.media.setVolume(self.sp.value())

if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
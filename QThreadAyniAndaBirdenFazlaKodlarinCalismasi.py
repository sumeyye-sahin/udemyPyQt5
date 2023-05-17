from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pytube import YouTube
import sys

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(500,100))
        self.setMaximumSize(QSize(500,100))
        self.setUI()
        self.show()

    def setUI(self):
        widget=QWidget()

        v_box=QVBoxLayout()
        h_box=QHBoxLayout()

        self.linkGiris=QLineEdit()
        self.linkGiris.setPlaceholderText("https://youtube.com/watch?v*")

        indirmeButonu=QPushButton("İNDİR")
        indirmeButonu.setCursor(QCursor(Qt.PointingHandCursor))
        indirmeButonu.clicked.connect(self.indirme)

        self.sonuc=QLabel()
        h_box.addWidget(self.linkGiris)
        h_box.addWidget(indirmeButonu)

        v_box.addLayout(h_box)
        v_box.addWidget(self.sonuc)

        widget.setLayout(v_box)
        self.setCentralWidget(widget)
    def indirme(self):
        indir=Download(self.linkGiris.text())
        indir.indir()

class Download(YouTube):
    def __init__(self,link):
        super().__init__(link)
    def indir(self):
        self.streams.first().download()

if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
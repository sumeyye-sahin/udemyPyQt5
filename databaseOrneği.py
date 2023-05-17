from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql  # veritabanı oluşturmak için import edilmesi gereken kütüphane
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def satabaseDB(self):
        #yeni bir database oluşturmak
        db=QtSql.QSqlDatabase.addDatabase('QSQLITE')  # db=QtSql.QSqlDatabase.addDatabase('hangi database i kullanmak istediğimizi belirtiyoruz')
        db.setDatabaseName('babies.db')
        if not db.open():
            QMessageBox.critical(self,'Hata','hata',QMessageBox.Cancel)
        sorgu=QtSql.QSqlQuery()
        sorgu.exec_('create table babies (id int primary key,isim varchar (20),soyisim varchar (20), dogunSaati varchar (5))')
        sorgu.exec_('insert into babies values(1,"Ayşe","Bakır","10.20")')


        self.model=QtSql.QSqlTableModel() #model objesi oluşturuldu
        self.model.setTable("babies") #modele hangi table ın ekleneceği yazılır
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0,Qt.Horizontal,'ID')
        self.model.setHeaderData(1,Qt.Horizontal,'Isim')
        self.model.setHeaderData(2,Qt.Horizontal,'Soyisim')
        self.model.setHeaderData(3,Qt.Horizontal,'Dogum Saati')

        view =QTableView()
        view.setModel(self.model)

        self.delrow=-1
        view.clicked.connect(self.satirAl)

        v_box=QVBoxLayout()
        btn1=QPushButton("satır ekle")
        btn2=QPushButton("satır sil")

        btn1.clicked.connect(self.satirEkle)
        btn2.clicked.connect(lambda: self.model.removeRow(view.currentIndex().row))
        v_box.addWidget(view)
        v_box.addWidget(btn1)
        v_box.addWidget(btn2)

        widget=QWidget()
        widget.setLayout(v_box)
        self.setCentralWidget(widget)

    def satirEkle(self):
        self.model.insertRow(self.model.rowCount(),1)

    def satirAl(self,i):
        self.delrow=i.row()

    def setUI(self):

        self.setWindowTitle("database")
        self.satabaseDB()
        self.show()

def main():
        app=QApplication(sys.argv)
        win=Window()
        sys.exit(app.exec())
if __name__=="__main__":
    main()
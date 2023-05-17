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
        model=QtSql.QSqlTableModel() #model objesi oluşturuldu
        #model.setTable("babies.db") #modele hangi table ın ekleneceği yazılır


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
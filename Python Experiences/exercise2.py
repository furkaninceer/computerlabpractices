import sys,os,sqlite3
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        self.Yazı_alanı=QtWidgets.QLineEdit()
        self.Temizle=QtWidgets.QPushButton("Temizle")
        self.kullanıcı_adı=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giriş=QtWidgets.QPushButton("Giriş")

        self.giriş.clicked.connect(self.login)
    def bağlantı(self):
        self.bağlantı=sqlite3.connect("üyeler.db")
        self.cursor=self.bağlantı.cursor()
        self.cursor.execute("Create Table ıf not exists üyeler(kullanıcı_adı TEXT,parola TEXT)")
        self.bağlantı.commit()
    def login(self):
        self.bağlantı=sqlite3.connect("üyeler.db")
        self.cursor=self.bağlantı.cursor()
        self.cursor.execute("Select adı,par from üyeler where adı=?,par=?",(self.kullanıcı_adı.text(),self.parola.text()))
        data=self.cursor.fetchall()
        if len(data)==0:
            self.Yazı_alanı.setText("Kullanıcı bulunamadı...")
        else:
            self.Yazı_alanı.setText("Giriş başarılı...")
        
        self.bağlantı.commit()

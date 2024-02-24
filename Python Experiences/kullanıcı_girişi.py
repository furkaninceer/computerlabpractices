import sys
from PyQt5 import QtWidgets
import sqlite3


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("Giriş")
        
        self.yazi_alani=QtWidgets.QLineEdit("")
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        self.giris.clicked.connect(self.login)
        self.setWindowTitle("kullanici girişi")
        self.setLayout(h_box)
        self.show()

        


    def baglanti_olustur(self):
        baglanti=sqlite3.connect("database.db")
        self.cursor=baglanti.cursor()
        self.cursor.execute("create table if not exists üyeler(kullanici_adi TEXT,parola TEXT)")
        baglanti.commit()
    def login(self):
        adi=self.kullanici_adi.text()
        par=self.parola.text()
        self.cursor.execute("Select * from üyeler kullanici_adi=? ,parola=?",(adi,par))
        data=self.cursor.fetchall()
        if len(data)==0:
            self.yazi_alani.setText("Kullanıcı kayıtlı değil")
        else:
            self.yazi_alani.setText("Hoşgeldiniz"+self.kullanici_adi.text())



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
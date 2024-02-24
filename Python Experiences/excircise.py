import sys,os,Sqlite3
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazı_alanı=QtWidgets.QLineEdit()
        self.temizle=QtWidgets.QPushButton("Temizle")
        self.kullanıcı_adı=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giriş=QtWidgets.QPushButton("Giriş")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.giriş.clicked.connect(self.login)
    def bağlantı_oluştur(self):
        self.bağlantı=Sqlite3.connect("üyeler.txt")
        self.cursor=self.bağlantı.cursor()
        self.cursor.execute("Create Table ıf not exists üyeler(kullanıcı_adı TEXT,parola TEXT)")
        self.bağlantı.commit()
    def login(self):
        self.bağlantı=Sqlite3.connect("üyeler.txt")
        self.cursor=self.bağlantı.cursor()
        self.cursor.execute("Select * from üyeler ")
        data=self.cursor.fetchall()
        for adı,par in data:
            if adı==self.kullanıcı_adı and par==self.parola:
                self.yazı_alanı.setText("Başarıyla giriş yapıldı")
            else:
                self.yazı_alanı.setText("Girdiğiniz bilgilere sahip kullanıcı bulunmuyor.")

    
        self.bağlantı.commit()
    def yaziyi_temizle(self):
        self.yazı_alanı.clear()
    def dosya_kaydet(self):
        dosya=QFileDialog.getSaveFile(self,"Dosya Kaydet",os.getnv("HOME"))
        with open(dosya[0],"r") as file:
            self.yazı_alanı.setText(file.read())
    def dosya_aç(self):
        dosya=QFileDialog.getOpenFile(self,"Dosya Aç",os.getnv("HOME"))
        with open(dosya[0],"r") as file:
            file.write(self.yazı_alanı.toPlainText())
class Menubar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere=Pencere()
        self.centralWidget(self.pencere)
        self.init_ui()
    def init_ui(self):  

        menubar=self.menubar()
        dosya=menubar.AddMenu("Dosya")
        düzenle=menubar.AddMenu("Düzenle")
        dosya_ac=QAction("Dosya Aç",self)
        dosya_kaydet=QAction("Dosya KAydet",self)
        cikis=QAction("cikis",self)
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)
        ara_ve_değiştir=düzenle.addMenu("ara_ve_değiştir")
        ara=QAction("Ara",self)
        değistir=QAction("değistir",self)
        ara_ve_değiştir.addAction(ara)
        ara_ve_değiştir.addAction(değistir)
        cikis.triggered.connect(self.cikis)
        dosya.triggered.connect(self.response)
    def dosya_kaydet(self):
        dosya=QFileDialog.getSaveFile(self,"Dosya Kaydet",os.getnv("HOME"))
        with open(dosya[0],"r") as file:
            self.yazı_alanı.setText(file.read())
    def dosya_aç(self):
        dosya=QFileDialog.getOpenFile(self,"Dosya Aç",os.getnv("HOME"))
        with open(dosya[0],"r") as file:
            file.write(self.yazı_alanı.toPlainText())

    def response(self,action):
        if action.text=="Dosya Aç":
            self.pencere.dosya_aç()
        elif action.text=="Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text=="cikis":
            qApp.Quit()



        


app = QtWidgets.QApplication(sys.argv)

menu = Menubar()

sys.exit(app.exec_())
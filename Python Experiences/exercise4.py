from PyQt5 import QtWidgets
import sys,os
import sqlite3
class Pencere(QtWidgets.QWidget):
    def __init__(self):
       super().__init__()
       self.init_ui() 

    def init_ui(self):

        self.ara_degistir=QtWidgets.QLineEdit()
        self.gonder=QtWidgets.QPushButton("Gönder")
        self.yazi_alani=QtWidgets.QTextEdit()
        self.parola=QtWidgets.QLineEdit()
        self.temizle=QtWidgets.QPushButton("Temizle")
        self.kaydet=QtWidgets.QPushButton("Kaydet")
        self.ac=QtWidgets.QPushButton("Aç")

        h_box=QtWidgets.QHBoxLayout()
        h_box.addWidget(self.ara_degistir)
        h_box.addWidget(self.gonder)

        h_box2=QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.temizle)
        h_box2.addWidget(self.kaydet)
        h_box2.addWidget(self.ac)

        v_box=QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box2)

        self.setLayout(v_box)
        
        self.setWindowTitle("Notepad")
        self.gonder.clicked.connect(self.Ara)
        self.temizle.clicked.connect(self.click)
        self.kaydet.clicked.connect(self.click)
        self.ac.clicked.connect(self.click)
    def baglantı_olustur(self):
        self.baglantı=sqlite3.connect("database.db")
        self.cursor=self.baglantı.cursor()
        self.cursor.execute("Create Table If Not Exists üyeler(parola TEXT)")
        self.baglantı.commit()
    def login(self):
        par=self.parola.text()
        self.cursor.execute("Select parola from üyeler where parola=?",(par,))
        data=self.cursor.fetchall()
        if len(data)==0:
            self.yazi_alani.setText("Giriş başarılı")
        else:
            self.yazi_alani.setText("Kullanıcı bulunamadı")
        
    def Ara(self):
        all_text=self.yazi_alani.text()
        text=self.ara_degistir.text()
        length=len(text)
        start=0
        end=start+length
        count=0
        while end<len(all_text):
            if all_text[start:end]==text:
                count+=1
        self.yazi_alani.setText(text+str(count)+"defa bulunuyor")
    def degistir(self):
        all_text=self.yazi_alani.text()
        text=self.ara_degistir.text()
        length=len(text)
        start=0
        end=start+length
        while end<len(all_text):
            if all_text[start:end]==text:
                pass

    def click(self):
        sender=self.sender()
        if sender.text()=="Temizle":
            self.yazi_alani.clear()
        elif sender.text()=="Kaydet":
            dosya = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
            with open(dosya[0],"w") as file:
                file.write(self.yazi_alani.toPlainText())
        elif sender.text()=="Aç":
            dosya = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
            with open(dosya[0],"r") as file:
                self.yazi_alani.setText(file.read())

class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere=Pencere()
        self.setCentralWidget(self.pencere)
        self.init_ui()
    def init_ui(self):
        
        menubar=self.menuBar()
        dosya=menubar.addMenu("Dosya")
        duzenle=menubar.addMenu("Düzenle")
        dosya_ac=QtWidgets.QAction("Dosya Aç",self)
        dosya_kaydet=QtWidgets.QAction("Dosya Kaydet",self)
        temizle=QtWidgets.QAction("Temizle",self)
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        ara_degistir=duzenle.addMenu("Ara Ve Değiştir")
        Ara=QtWidgets.QAction("Ara",self)
        degistir=QtWidgets.QAction("Degiştir",self)
        ara_degistir.addAction(Ara)
        ara_degistir.addAction(degistir)

        dosya.triggered.connect(self.response)
        ara_degistir.triggered.connect(self.settings)

    def response(self,action):
        if action.text()=="Dosya Aç":
            self.pencere.ac_click()
        elif action.text()=="Dosya Kaydet":
            self.pencere.kaydet_click
        elif action.text()=="Temizle":
            self.pencere.yazi_alani.clear()
    def settings(self,action):
        if action.text()=="Ara":
            self.pencere.Ara()
        elif action.text()=="Değiştir":
            self.pencere.degistir()



app = QtWidgets.QApplication(sys.argv)

menu = Menu()
menu.show()

sys.exit(app.exec_())





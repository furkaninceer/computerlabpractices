import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QLineEdit

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.yazi_alani = QTextEdit()
        self.ara= QLineEdit()
        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addWidget(self.ara)
        v_box.addWidget(self.yazi_alani)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)




    def yaziyi_temizle(self):
        self.yazi_alani.clear()

    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))

        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())

    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))

        with open(dosya_ismi[0],"w") as file:

            file.write(self.yazi_alani.toPlainText())
    def Ara(self):
        writing = self.yazi_alani.toPlainText()
        text =self.ara.text()
        length = len(text)
        length2 = len(writing)
        a = 0
        last_char = a + length
        Count = 0

        while a <= length2 - length: 
            if text == writing[a:last_char]:
                Count += 1
            a += 1

        self.yazi_alani.setText(f'The text "{text}" appears {Count} times.')



class Menu(QMainWindow):

    def __init__(self):

        super().__init__()


        self.pencere = Notepad()

        self.setCentralWidget(self.pencere)


        self.menuleri_olustur()
    def menuleri_olustur(self):

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle=menubar.addMenu("Duzenle")

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)

        dosya_kaydet.setShortcut("Ctrl+S")

        temizle = QAction("Dosyayı Temizle",self)
        temizle.setShortcut("Ctrl+D")

        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        ara_degistir=duzenle.addMenu("Ara ve Degistir")

        Ara=QAction("Ara",self)
        Ara.setShortcut("Ctrl+A")

        degistir=QAction("Değistir",self)
        degistir.setShortcut("Ctrl+D")

        ara_degistir.addAction(Ara)
        ara_degistir.addAction(degistir)

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)
        ara_degistir.triggered.connect(self.settings)

        self.setWindowTitle("Metin Editörü")

        self.show()
    def settings(self,action):
        if action.text()=="Ara":
            self.pencere.Ara()
        elif action.text()=="Değiştir":
            self.pencere.A()
    def response(self,action):

        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()

        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "Dosyayı Temizle":
            self.pencere.yaziyi_temizle()

        elif action.text() == "Çıkış":
            qApp.quit()








app = QApplication(sys.argv)

menu = Menu()


sys.exit(app.exec_())
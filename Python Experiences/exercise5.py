from PyQt5 import QtWidgets
import os,sys
class Soccer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.player_one=QtWidgets.QLineEdit("")
        self.player_two=QtWidgets.QLineEdit("")
        self.player_three=QtWidgets.QLineEdit("")
        self.player_four=QtWidgets.QLineEdit("")
        self.player_five=QtWidgets.QLineEdit("")
        self.player_six=QtWidgets.QLineEdit("")
        self.player_seven=QtWidgets.QLineEdit("")
        self.player_eight=QtWidgets.QLineEdit("")
        self.player_nine=QtWidgets.QLineEdit("")
        self.player_ten=QtWidgets.QLineEdit("")
        self.player_eleven=QtWidgets.QLineEdit("")

        V_Box=QtWidgets.QVBoxLayout()
        H_Box=QtWidgets.QVBoxLayout()
        H_Box2=QtWidgets.QVBoxLayout()
        H_Box3=QtWidgets.QVBoxLayout()

        H_Box.addWidget(self.player_one)
        H_Box.addWidget(self.player_two)
        H_Box.addWidget(self.player_three)
        H_Box.addWidget(self.player_four)
        H_Box2.addWidget(self.player_five)
        H_Box2.addWidget(self.player_six)
        H_Box2.addWidget(self.player_seven)
        H_Box2.addWidget(self.player_eight)
        H_Box3.addWidget(self.player_nine)
        H_Box3.addWidget(self.player_ten)
        H_Box3.addWidget(self.player_eleven)

        V_Box.addLayout(H_Box)
        V_Box.addStretch()
        V_Box.addLayout(H_Box2)
        V_Box.addStretch()
        V_Box.addLayout(H_Box3)

app = QtWidgets.QApplication(sys.argv)

soccer = Soccer()

sys.exit(app.exec_())
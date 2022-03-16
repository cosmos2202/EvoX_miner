import os

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 540)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #5E338D;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setGeometry(QtCore.QRect(584, 342, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_ok.setFont(font)
        self.button_ok.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_ok.setObjectName("button_ok")
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setGeometry(QtCore.QRect(470, 342, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_cancel.setFont(font)
        self.button_cancel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_cancel.setObjectName("button_cancel")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(250, 432, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_start.setFont(font)
        self.button_start.setStyleSheet("background-color: rgb(204, 109, 179);")
        self.button_start.setObjectName("button_start")
        self.wallet = QtWidgets.QLabel(self.centralwidget)
        self.wallet.setGeometry(QtCore.QRect(90, 140, 280, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.wallet.setFont(font)
        self.wallet.setStyleSheet("color: rgb(255, 255, 255);")
        self.wallet.setObjectName("wallet")
        self.pool = QtWidgets.QLabel(self.centralwidget)
        self.pool.setGeometry(QtCore.QRect(90, 230, 280, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pool.setFont(font)
        self.pool.setStyleSheet("color: rgb(255, 255, 255);")
        self.pool.setObjectName("pool")
        self.text_wallet = QtWidgets.QTextEdit(self.centralwidget)
        self.text_wallet.setGeometry(QtCore.QRect(90, 190, 611, 31))
        self.text_wallet.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_wallet.setObjectName("text_wallet")
        self.text_wallet_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_wallet_2.setGeometry(QtCore.QRect(90, 280, 611, 31))
        self.text_wallet_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_wallet_2.setObjectName("text_wallet_2")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(66, 30, 671, 91))
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("resurs/img/logo.png"))
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 520, 251, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EvoX Miner"))
        self.button_ok.setText(_translate("MainWindow", "OK"))
        self.button_ok.clicked.connect(self.ok)
        self.button_cancel.setText(_translate("MainWindow", "Cancel"))
        self.button_cancel.clicked.connect(self.cancel)
        self.button_start.setText(_translate("MainWindow", "Start EvoX Miner"))
        self.button_start.clicked.connect(self.start)
        self.wallet.setText(_translate("MainWindow", "Your Wallet:"))
        self.pool.setText(_translate("MainWindow", "Your Pool:"))
        self.label.setText(_translate("MainWindow", "Specially for Evolution Network from cosmos"))

    def start(self):
        os.startfile(r'resurs\xmrig\xmrig.exe')

    def cancel(self):
        sys.exit()

    def ok(self):
        wallet = self.text_wallet.toPlainText()
        pool = self.text_wallet_2.toPlainText()
        settings_end = []
        pools = {}
        import json
        with open(r'resurs\xmrig\config.json', 'r+') as file:
            config = json.load(file)
            config['pools'][0]['url'] = pool
            config['pools'][0]['user'] = wallet
        with open(r'resurs\xmrig\config.json', 'w') as file:
            json.dump(config, file)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import os

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWinExtras import QtWin


import multiprocessing
quantity_threads = multiprocessing.cpu_count()

user = open(r'resurs\user.txt', 'r+').read().split(',')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 520)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(250, 430, 270, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_start.setFont(font)
        self.button_start.setStyleSheet("background-color: #66FBFF;\n"
"border: 1px solid #AB1E24;\n"
"")
        self.button_start.setObjectName("button_start")
        self.wallet = QtWidgets.QLabel(self.centralwidget)
        self.wallet.setGeometry(QtCore.QRect(90, 160, 610, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.wallet.setFont(font)
        self.wallet.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
"color: #D7D7D7;")
        self.wallet.setObjectName("wallet")
        self.pool = QtWidgets.QLabel(self.centralwidget)
        self.pool.setGeometry(QtCore.QRect(90, 240, 610, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pool.setFont(font)
        self.pool.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
"color: #D7D7D7;")
        self.pool.setObjectName("pool")
        self.text_wallet = QtWidgets.QTextEdit(self.centralwidget)
        self.text_wallet.setGeometry(QtCore.QRect(90, 200, 610, 30))
        self.text_wallet.setStyleSheet("background-color: #D7D7D7;")
        self.text_wallet.setObjectName("text_wallet")
        self.text_wallet_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_wallet_2.setGeometry(QtCore.QRect(90, 280, 320, 30))
        self.text_wallet_2.setStyleSheet("background-color: #D7D7D7;")
        self.text_wallet_2.setObjectName("text_wallet_2")
        self.cpu = QtWidgets.QTextEdit(self.centralwidget)
        self.cpu.setGeometry(QtCore.QRect(90, 370, 160, 30))
        self.cpu.setStyleSheet("background-color: #D7D7D7;\n"
"")
        self.cpu.setObjectName("cpu")
        self.cpuload = QtWidgets.QLabel(self.centralwidget)
        self.cpuload.setGeometry(QtCore.QRect(90, 330, 610, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.cpuload.setFont(font)
        self.cpuload.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
"color: #D7D7D7;")
        self.cpuload.setObjectName("cpuload")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(50, 20, 128, 128))
        self.logo.setStyleSheet("background: rgba(0, 0, 0, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("resurs/img/128x128.png"))
        self.logo.setObjectName("logo")
        self.wallet_2 = QtWidgets.QLabel(self.centralwidget)
        self.wallet_2.setGeometry(QtCore.QRect(200, 70, 550, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.wallet_2.setFont(font)
        self.wallet_2.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
"color: #D7D7D7;")
        self.wallet_2.setObjectName("wallet_2")
        self.fon = QtWidgets.QLabel(self.centralwidget)
        self.fon.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.fon.setText("")
        self.fon.setPixmap(QtGui.QPixmap("resurs/img/bch.jpg"))
        self.fon.setObjectName("fon")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 500, 240, 15))
        self.label.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
"color: #D7D7D7;")
        self.label.setObjectName("label")
        self.fon.raise_()
        self.button_start.raise_()
        self.wallet.raise_()
        self.pool.raise_()
        self.text_wallet.raise_()
        self.text_wallet_2.raise_()
        self.cpu.raise_()
        self.cpuload.raise_()
        self.logo.raise_()
        self.wallet_2.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EvoX Miner"))
        self.button_start.setText(_translate("MainWindow", "Start EvoX Miner"))
        self.button_start.clicked.connect(self.start)
        self.wallet.setText(_translate("MainWindow", "Your Wallet:"))
        self.pool.setText(_translate("MainWindow", "Your Pool:"))
        self.cpuload.setText(_translate("MainWindow", "Threads:"))
        self.wallet_2.setText(_translate("MainWindow", "EvoX Xmrig GUI Easy Miner"))
        self.label.setText(_translate("MainWindow", "Specially for evolution-network.org made Cosmos"))
        self.text_wallet_2.setText(user[1])
        self.text_wallet.setText(user[0])
        self.cpu.setText(user[2])


    def start(self):
        wallet = self.text_wallet.toPlainText()
        pool = self.text_wallet_2.toPlainText()
        threads = int(self.cpu.toPlainText())
        ithreads = []
        if threads >= quantity_threads:
            for i in range(quantity_threads):
                ithreads.append(i)
        else:
            for i in range(threads):
                ithreads.append(i)
        import json
        with open(r'resurs\xmrig\config.json', 'r+') as file:
            config = json.load(file)
            config['pools'][0]['url'] = pool
            config['pools'][0]['user'] = wallet
            config['cpu']['rx/arq'] = ithreads

        with open(r'resurs\xmrig\config.json', 'w') as file:
            json.dump(config, file)
        rec = wallet + "," + pool + "," + str(threads)
        user = open(r'resurs\user.txt', 'w')
        user.write(rec)

        os.startfile(r'resurs\xmrig\xmrig.exe')
        sys.exit()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
    apps = QtWidgets.QApplication(sys.argv)
    apps.setWindowIcon(QtGui.QIcon('resurs\img\icon.ico'))
    window = QtWidgets.QWidget()
    window.setWindowIcon(QtGui.QIcon('resurs\img\icon.ico'))
    MainWindow.show()
    sys.exit(app.exec_())
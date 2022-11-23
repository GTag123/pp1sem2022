from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-30, 190, 441, 20))
        self.line.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.text_bot = QtWidgets.QLabel(self.centralwidget)
        self.text_bot.setGeometry(QtCore.QRect(0, 0, 401, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_bot.sizePolicy().hasHeightForWidth())
        self.text_bot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.text_bot.setFont(font)
        self.text_bot.setStyleSheet("")
        self.text_bot.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_bot.setObjectName("text_bot")
        self.text_bot_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_bot_2.setGeometry(QtCore.QRect(0, 200, 401, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_bot_2.sizePolicy().hasHeightForWidth())
        self.text_bot_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.text_bot_2.setFont(font)
        self.text_bot_2.setStyleSheet("")
        self.text_bot_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_bot_2.setObjectName("text_bot_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 270, 401, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 310, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 321, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_bot.setText(_translate("MainWindow", "Бот"))
        self.text_bot_2.setText(_translate("MainWindow", "Пользователь"))
        self.pushButton.setText(_translate("MainWindow", "Пуск!"))
        # self.label.setText(_translate("MainWindow", "тут будет ебучий текст (этот ебучий плэйсхолдер скрыть до запуска проги)"))

    def changeBotText(self, text):
        self.label.setText(text)

def startGui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    startGui()
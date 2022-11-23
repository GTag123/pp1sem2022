from PyQt6 import QtCore, QtGui, QtWidgets
from design import *
import threading
from bot import Bot
from time import sleep
import sys

uicommon = 0

def botInit():
    global uicommon
    failed = 0
    while uicommon == 0:
        if failed > 9:
            print("UI failed")
            return
        sleep(1)
        failed += 1

    bot = Bot(uicommon)
    while True:
        try:
            bot.callback()
            sleep(0.1)
        except:
            print("Произошла ошибка. Попробуйте снова")
            bot = Bot(uicommon, True)


def rendering():
    global uicommon
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    uicommon = ui
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())



t1 = threading.Thread(target=rendering, args=())
t1.start()

t2 = threading.Thread(target=botInit, args=())
t2.start()
print(1)

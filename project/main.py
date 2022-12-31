from PyQt6 import QtCore, QtGui, QtWidgets
from design import *
import threading
from bot import Bot
from time import sleep
import sys

uicommon = 0  # default null
voiceBtn = 0  # 0 - first push, 1 - second push
querybuffer = []
def botcallback(botobj, event):
    global voiceBtn
    global uicommon
    print("botcallback tread started")
    while uicommon == 0:
        print("uierror in botcallback")
        sleep(0.2)
    uicommon.inActivateText()
    isRecognized = False
    while isRecognized == False:
        isRecognized = botobj.callback("", event)
        if event.is_set():
            break
        # sleep(0.1)
    uicommon.ActivateText()
    voiceBtn = 0
    print("botcallback tread end")

def bottext(botobj, text):
    global querybuffer
    global uicommon
    print("bottext tread started")
    while uicommon == 0:
        print("uierror in botcallback")
        sleep(0.2)
    uicommon.changeUserInputtedText(text)
    isRecognized = botobj.callback(text)
    del querybuffer[:]
    print("bottext tread end")



def rendering():
    global uicommon
    global querybuffer
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    uicommon = Ui_MainWindow()
    uicommon.setupUi(MainWindow)
    MainWindow.show()
    botobj = Bot(uicommon, False, querybuffer)
    exitVoiceEvent = threading.Event()
    def onBtn2push():
        global voiceBtn
        if voiceBtn == 1:
            exitVoiceEvent.set()
            voiceBtn = 0
        else:
            uicommon.changeBotText("Говорите")
            uicommon.changeUserInputtedText("")
            threading.Thread(target=botcallback, args=(botobj, exitVoiceEvent)).start()
            voiceBtn = 1

    def onPush():
        querybuffer.append(uicommon.lineEdit.text().lower().strip())
        uicommon.lineEdit.setText("")
        if len(querybuffer) == 1:
            threading.Thread(target=bottext, args=(botobj, querybuffer[-1])).start()

    uicommon.pushButton_2.clicked.connect(onBtn2push)
    uicommon.pushButton.clicked.connect(onPush)
    sys.exit(app.exec())


t1 = threading.Thread(target=rendering, args=())
# t2 = threading.Thread(target=botInit, args=())
# t2.start()
t1.start()
t1.join()

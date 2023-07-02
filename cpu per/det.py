import PyQt5
import sys
from PyQt5.QtCore import *
from PyQt5.QtDesigner import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from detlay import Ui_MainWindow
import psutil
import platform
import time


class main2(QThread):
    def __init__(self):
        super(main2,self).__init__()
    
    def run(self):
        while True:
            text1 = str(psutil.cpu_percent())
            text2 = str(psutil.cpu_freq())
            text3 = str(psutil.cpu_count())
            text4 = str(psutil.cpu_stats())
            ak.cpu_per(text1)
            ak.cpu_fre(text2)
            ak.cpu_stat(text4)
            ak.cpu_cou(text3)
            time.sleep(0.5)

m2 = main2()

class main(QMainWindow):
    def __init__(self):
        super(main,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        m2.start()

    def cpu_per(self,text):
        self.ui.label_2.setText(text)
    def cpu_fre(self,text):
        self.ui.label_5.setText(text)
    def cpu_stat(self,text):
        self.ui.label_8.setText(text)
    def cpu_cou(self,text):
        self.ui.label_9.setText(text)


if __name__=="__main__":
    app = QApplication(sys.argv)
    ak = main()
    ak.show()
    sys.exit(app.exec_())


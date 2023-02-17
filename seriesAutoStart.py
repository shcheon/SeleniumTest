import sys

from seriesAuto import Ui_MainWindow
from PyQt5.QtWidgets import *

class autoStart(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])
sn = autoStart()
QApplication.processEvents()
sys.exit(app.exec_())

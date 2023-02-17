from PyQt5.QtCore import QThread

from TestAutomation.admin.InitUserDevice.InitUserDeviceService import InitUserDeviceService
from TestAutomation.admin.InitUserDevice.InitUserDeviceVO import InitUserDeviceVO


class InitUserDeviceController(QThread):
    def __init__(self, parent, console, userId, userPassword, resetUser, mode=''):
        QThread.__init__(self, parent)
        self.console = console
        self.mode = mode
        self.vo = InitUserDeviceVO(userId, userPassword, resetUser)

    def run(self):
        InitUserDeviceService(self.console, self.vo, self.mode).execute()


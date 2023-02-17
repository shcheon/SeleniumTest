from PyQt5.QtCore import QThread

from TestAutomation.template import TemplateVO, TemplateService


class TemplateController(QThread):
    def __init__(self, parent, console, arg1, arg2, mode=''):
        QThread.__init__(self, parent)
        self.console = console
        self.mode = mode
        self.vo = TemplateVO(arg1, arg2)

    def run(self):
        TemplateService(self.console, self.vo, self.mode).execute()


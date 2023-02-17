from datetime import datetime


class LoggerUtil:
    def __init__(self, console):
        self.console = console

    def _print_console(self, msg):
        if self.console:
            self.console.append('[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '] ' + msg)
        print('[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '] ' + msg)

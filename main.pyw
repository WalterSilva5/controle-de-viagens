from model.ModelTela import ModelTela
from controller.ControllerTela import ControllerTela
from PyQt5.QtWidgets import QApplication

import sys

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = ModelTela()
        self.view = ControllerTela(self.model)
        self.view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())
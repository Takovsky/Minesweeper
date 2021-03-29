# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtWidgets import QApplication
from window import Window

if __name__ == "__main__":
    app = QApplication([])
    widget = Window()
    widget.show()
    sys.exit(app.exec_())

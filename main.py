# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication
from window import Window
from scene import Scene

if __name__ == "__main__":
    app = QApplication([])
    scene = Scene()
    scene.setScene()
    scene.showScene()
    sys.exit(app.exec_())

import sys
import os

from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from field import Field
from game_configuration import GameConfiguration
from gameboard import Gameboard


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
        self.drawGameboard()

    def initUI(self):
        self.setWindowTitle("Minesweeper")

        self.gameConfiguration = GameConfiguration()

        self.layout = QGridLayout(self)

        ## tego chyba nie qmam
        self.layout.setColumnStretch(1, 1)
        self.layout.setRowStretch(1, 1)
        
        self.layout.addWidget(self.gameConfiguration,0 ,0)
        self.setFixedSize(800, 600)

    def drawGameboard(self):
        self.gameboard = Gameboard(self.gameConfiguration)
        self.layout.addWidget(self.gameboard, 1, 0)

    layout = None
    gameConfiguration = None
    gameboard = None
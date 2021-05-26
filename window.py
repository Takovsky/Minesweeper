import sys
import os

from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from field import Field
from game_configuration import GameConfiguration
from gameboard import Gameboard
from game import Game
from game_configuration import GameConfiguration

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

    def set(self, game):
        self.setWindowTitle("Minesweeper")
        self.setMinimumSize(640, 480)

        gameConf = game.getGameConfiguration()
        self.__gameboard = game.getGameboard()

        self.resizeWindow(gameConf)

        self.__layout = QGridLayout(self)
        gameConf.setFixedHeight(150)
        gameConf.setMaximumHeight(100)
        self.__layout.addWidget(gameConf, 0, 0)
        self.__layout.addWidget(self.__gameboard, 1, 0)

    def resizeWindow(self, gameConf):
        size = gameConf.getSize() * 25

        self.__gameboard.setFixedSize(size, size)

        if size > 380:
            self.setFixedSize(size+25, size + 125)        

    __layout = None
    __gameboard = None
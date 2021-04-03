from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit
from game_configuration import GameConfiguration
from field import Field

class Gameboard(QWidget):
    def __init__(self):
        super(Gameboard, self).__init__()
        self.__layout = QGridLayout(self)

    def clearLayout(self):
        while self.__layout.count():
            child = self.__layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def resetGameboard(self):
        self.__mines = None
        self.__size = None
        self.clearLayout()
        self.__fieldsArray = []

    def setGameboard(self, gameConfiguration):
        self.resetGameboard()

        self.__mines = gameConfiguration.getMines()
        self.__size = gameConfiguration.getSize()
        self.initArray(gameConfiguration)

    def initArray(self, gameConfiguration):
        for i in range(self.__size):
            secondDimention = []
            for j in range(self.__size):
                field = Field()
                secondDimention.append(field)
                self.__layout.addWidget(field, i, j)
                self.__layout.setSpacing(0)
            self.__fieldsArray.append(secondDimention)

    __fieldsArray = []
    __layout = None
    __mines = None
    __size = None

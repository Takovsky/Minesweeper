from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit
from game_configuration import GameConfiguration
from field import Field

class Gameboard(QWidget):
    def __init__(self, gameConfiguration):
        super(Gameboard, self).__init__()

        self.mines = gameConfiguration.getMines()
        self.size = gameConfiguration.getSize()

        self.initLayout()
        self.initArray(gameConfiguration)

    def initArray(self, gameConfiguration):
        for i in range(self.size - 1):
            secondDimention = []
            for j in range(self.size - 1):
                field = QPushButton()
                secondDimention.append(field)
                self.layout.addWidget(field, i, j)
                self.layout.setSpacing(0)
            self.fieldsArray.append(secondDimention)

    def initLayout(self):
        self.layout = QGridLayout(self)
        self.layout.setRowStretch(self.size, self.size)
        self.layout.setColumnStretch(self.size, self.size)

    fieldsArray = []
    layout = None
    mines = None
    size = None
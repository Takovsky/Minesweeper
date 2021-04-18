from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit
from game_configuration import GameConfiguration
from field import Field
import random
from coordinates import Coordinates


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
        self.__boardGenerated = False

    def setGameboard(self, gameConfiguration):
        self.resetGameboard()

        self.__mines = gameConfiguration.getMines()
        self.__size = gameConfiguration.getSize()
        self.initArray(gameConfiguration)

    def initArray(self, gameConfiguration):
        for i in range(self.__size):
            secondDimention = []
            for j in range(self.__size):
                field = Field(self, i, j)
                secondDimention.append(field)
                self.__layout.addWidget(field, i, j)
                self.__layout.setSpacing(0)
            self.__fieldsArray.append(secondDimention)

    def findNeighbors(self, field):
        neighbors = []

        x, y = field.getCoordinates().getCoordinates()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if(i < 0 or i > self.__size - 1 or
                   j < 0 or j > self.__size - 1 or
                   (i == x and j == y)):
                    continue

                neighbors.append(Coordinates(i, j))

        return neighbors

    ## tutaj brakuje odkrycia pol sasiadujacych jesli mamy juz odkryte miny dookola
    # def uncoverFieldsNearby(self, field, neighbors):

    def onFieldClicked(self, field):
        if self.__boardGenerated == False:
            self.generateBoard(field)
            self.__boardGenerated = True

        neighbors = self.findNeighbors(field)
        # self.uncoverFieldsNearby(field, neighbors)

    def generateBoard(self, field):
        field.setValue(0)
        self.generateMines(field.getCoordinates())
        self.generateRestFields()

    def generateMines(self, coordinates):
        x, y = coordinates.getCoordinates()
        for i in range(self.__mines):
            mineX = x
            mineY = y
            while self.isMineOverlaping(x, y, mineX, mineY) == True:
                mineX = random.randint(0, self.__size - 1)
                mineY = random.randint(0, self.__size - 1)
            field = self.__fieldsArray[mineX][mineY]
            field.setValue("M")
            ## linijka nizej odkrywa pole - tylko dla debugu
            field.setFieldVisible()

    def isMineOverlaping(self, x, y, mineX, mineY):
        if (x - 1 <= mineX and x + 1 >= mineX and
                y - 1 <= mineY and y + 1 >= mineY):
            return True

        if (self.__fieldsArray[mineX][mineY].getValue() == "M"):
            return True

        return False

    def generateRestFields(self):
        for fields in self.__fieldsArray:
            for field in fields:
                if (field.getValue() == None):
                    value = self.calculateFieldValue(field)
                    field.setValue(value)
                    ## linijka nizej odkrywa pole - tylko dla debugu
                    field.setFieldVisible()

    def calculateFieldValue(self, field):
        x, y = field.getCoordinates().getCoordinates()
        mines = 0
        neighbors = self.findNeighbors(field)

        for neighbor in neighbors:
            x, y = neighbor.getCoordinates()
            field = self.__fieldsArray[x][y]
            if(field.getValue() == "M"):
                mines += 1

        return mines

    __fieldsArray = []
    __layout = None
    __mines = None
    __size = None
    __boardGenerated = False

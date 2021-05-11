from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
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
        label1 = QLabel()
        label1.setText("Mines left: ")
        self.__minesLeftLabel = QLabel()
        self.__minesLeftLabel.setText(str(self.__mines))

        self.__layout.addWidget(label1, 0, 0, 1, 3)
        self.__layout.addWidget(self.__minesLeftLabel, 0, 3, 1, 3)

        for i in range(self.__size):
            secondDimention = []
            for j in range(self.__size):
                field = Field(self, i, j)
                secondDimention.append(field)
                self.__layout.addWidget(field, i + 1, j)
                self.__layout.setSpacing(0)
            self.__fieldsArray.append(secondDimention)

    def getFieldsArray(self):
        return self.__fieldsArray

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

    def uncoverFieldsNearby(self, field, neighbors):
        coveredMines = 0
        for neighbor in neighbors:
            fieldToUncover = self.__fieldsArray[neighbor.getX(
            )][neighbor.getY()]
            if fieldToUncover.isCovered():
                coveredMines += 1

        fieldsToUncover = []

        if coveredMines >= field.getValue():
            for neighbor in neighbors:
                fieldToUncover = self.__fieldsArray[neighbor.getX(
                )][neighbor.getY()]
                if fieldToUncover.isChecked() == True:
                    continue
                if fieldToUncover.getValue() != 0 and fieldToUncover.getValue() != "M":
                    fieldToUncover.setFieldVisible()
                elif fieldToUncover.isCovered() == False:
                    fieldsToUncover.append(fieldToUncover)

                if fieldToUncover.isCovered() == False:
                    fieldToUncover.setChecked(True)

        for fieldToUncover in fieldsToUncover:
            self.onFieldClicked(fieldToUncover)

    def isGameLost(self, field):
        return field.getValue() == "M"

    def tearDownLostGame(self, field):
        for fields in self.__fieldsArray:
            for f in fields:
                if f.getValue() == "M":
                    f.setFieldVisible()
                if f.isChecked() == False and f.isCovered() == False:
                    f.markUnchecked()
                f.setEnabled(False)

        field.markFailed()

    def isGameWon(self):
        checkedFields = 0
        coveredFields = 0
        coveredMines = 0
        for fields in self.__fieldsArray:
            for field in fields:
                if field.isChecked():
                    checkedFields += 1
                if field.isCovered():
                    coveredFields += 1
                    if field.getValue() == "M":
                        coveredMines += 1

        ret = (checkedFields + coveredFields == self.__size * self.__size or
               coveredMines == self.__mines or
               checkedFields == self.__size * self.__size - self.__mines)

        return ret

    def tearDownWonGame(self):
        for fields in self.__fieldsArray:
            for field in fields:
                if (field.isChecked() == False and field.isCovered() == False
                        and field.getValue() == "M"):
                    field.toggleCover()
                elif field.isChecked() == False and field.isCovered() == False:
                    field.setFieldVisible()

                field.setEnabled(False)

        self.updateLeftMines()

    def onFieldClicked(self, field):
        if self.__boardGenerated == False:
            self.generateBoard(field)
            self.__boardGenerated = True

        field.setFieldVisible()

        if self.isGameLost(field):
            self.tearDownLostGame(field)
            return

        neighbors = self.findNeighbors(field)
        self.uncoverFieldsNearby(field, neighbors)

        if self.isGameWon():
            self.tearDownWonGame()

    def updateLeftMines(self):
        leftMines = self.__mines
        for fields in self.__fieldsArray:
            for field in fields:
                if field.isCovered() == True:
                    leftMines -= 1

        self.__minesLeftLabel.setText(str(leftMines))

    def generateBoard(self, field):
        if field.isChecked() == True:
            field.setValue(0)

        self.generateMines(field.getCoordinates())
        self.generateRestFields()
        self.__boardGenerated = True

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
    __minesLeftLabel = None

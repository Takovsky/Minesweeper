from PySide2.QtWidgets import QWidget, QPushButton
from numberToColor import NumberToColor
from coordinates import Coordinates
from PySide2.QtCore import Qt


class Field(QPushButton):
    def __init__(self, gameboard, x, y):
        super(Field, self).__init__()
        self.__gameboard = gameboard
        self.__coordinates = Coordinates(x, y)
        self.setCheckable(True)
        self.setFixedSize(25, 25)

    def mousePressEvent(self, event):
        leftButton = event.button() == Qt.LeftButton
        if leftButton == False and self.isChecked() == False:
            self.toggleCover()
            self.__gameboard.updateLeftMines()
        elif self.__isCovered == False:
            self.setChecked(True)
            self.__gameboard.onFieldClicked(self)

    def toggleCover(self):
        self.__isCovered = self.__isCovered == False
        text = ""
        if self.__isCovered:
            text = "C"

        self.setText(text)
        self.setColor(text)

    def setFieldVisible(self):
        if self.__isCovered:
            return
        if self.__value != 0:
            self.setText(str(self.__value))
            self.setColor(self.__value)

    def setColor(self, val):
        numbToColor = NumberToColor()
        styleSheet = self.generateStyleSheet(
            numbToColor.getDictionary().get(val, "black"))
        self.setStyleSheet(styleSheet)

    def generateStyleSheet(self, val):
        return "color: " + val + ";" + "font: bold"

    def getValue(self):
        return self.__value

    def setValue(self, val):
        self.__value = val

    def getCoordinates(self):
        return self.__coordinates

    def isVisible(self):
        return self.__isVisible

    def isCovered(self):
        return self.__isCovered

    __value = None
    __gameboard = None
    __coordinates = None
    __isCovered = False

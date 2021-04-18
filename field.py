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
        if event.button() == Qt.RightButton:
            print(
                "tutaj trzeba dodac obsluge prawego przysku, jako przykrycie miny mozna uzyc \"O\"")
        else:
            self.__gameboard.onFieldClicked(self)
            self.setFieldVisible()

    def setFieldVisible(self):
        self.__isVisible = True
        self.setEnabled(False)
        self.setChecked(True)
        if(self.__value != 0):
            self.setText(str(self.__value))
            self.setColor()

    def setColor(self):
        numbToColor = NumberToColor()
        styleSheet = self.generateStyleSheet(
            numbToColor.getDictionary()[self.__value])
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

    __value = None
    __gameboard = None
    __coordinates = None
    __isVisible = False

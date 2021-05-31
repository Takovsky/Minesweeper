from random import randint
from typing import List
from time import sleep
from datetime import datetime, timedelta
from threading import Timer
from field import Field
from vector import Vector
from move import Move


class RandomSolver():
    def __init__(self, game):
        super(RandomSolver, self).__init__()
        self.__game = game
        self.__gameboard = self.__game.getGameboard()
        self.__gameConfiguration = self.__game.getGameConfiguration()
        self.__fieldsArray: List[Field] = []
    
    def set(self):
        self.__gameboard.setGameboard(self.__gameConfiguration)

        self.__fieldsArray = []
        for fields in self.__gameboard.getFieldsArray():
            for field in fields:
                self.__fieldsArray.append(field)
        start_field = randint(0, len(self.__fieldsArray) - 1)
        startingField = self.__fieldsArray[start_field]
        
        self.__counter = 1
        self.__gameboard.onFieldClicked(startingField)

        self.updateFieldsArray()
    
    def run(self):
        while len(self.__fieldsArray) > self.__gameConfiguration.getMines():
            self.__counter += 1
            field_number = randint(0, len(self.__fieldsArray) - 1)
            field = self.__fieldsArray[field_number]
            self.__gameboard.onFieldClicked(field)
            self.updateFieldsArray()
            if self.__gameboard.isGameLost(field):
                break

    def updateFieldsArray(self):
        fieldsToRemove = []
        for field in self.__fieldsArray:
            if field.isChecked() == True:
                fieldsToRemove.append(field)
        for field in fieldsToRemove:
            self.__fieldsArray.remove(field)
        
    def getResult(self):
        separator = ";"
        newLine = "\n"

        return str(self.__counter) + separator + str(self.__game.isWon()) + newLine


    __counter = 0
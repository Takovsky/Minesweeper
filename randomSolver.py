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
        self.__timer = Timer(interval=2, function=self.performNextMove)

        ## todo: 
        ## get gameboard from game
        ## gameboard.onFieldClicked(field)
    
    def set(self):
        #set gameboard
        self.__gameboard.setGameboard(self.__gameConfiguration)

        #perform first random move to generate initial board configuration
        self.__fieldsArray = []
        for fields in self.__gameboard.getFieldsArray():
            for field in fields:
                self.__fieldsArray.append(field)
        start_field = randint(0, len(self.__fieldsArray) - 1)
        startingField = self.__fieldsArray[start_field]
        self.__gameboard.onFieldClicked(startingField)

        self.updateFieldsArray()
    
    def run(self):
        counter = 1
        while len(self.__fieldsArray) > self.__gameConfiguration.getMines():
            counter += 1
            self.performNextMove()
            # self.__timer = Timer(interval=2, function=self.performNextMove)
            # self.__timer.start()

        print("len2: " + str(len(self.__fieldsArray)))
        print("COUNTER: " + str(counter))

    def performNextMove(self):
        print("len: " + str(len(self.__fieldsArray)))
        field_number = randint(0, len(self.__fieldsArray) - 1)
        field = self.__fieldsArray[field_number]
        self.__gameboard.onFieldClicked(field)
        self.updateFieldsArray()

    def updateFieldsArray(self):
        fieldsToRemove = []
        for field in self.__fieldsArray:
            if field.isChecked() == True:
                fieldsToRemove.append(field)
        for field in fieldsToRemove:
            self.__fieldsArray.remove(field)
        

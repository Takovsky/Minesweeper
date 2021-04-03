from game_configuration import GameConfiguration
from gameboard import Gameboard

class Game():
    def __init__(self):
        super(Game, self).__init__()

    def set(self):
        self.__gameConfiguration = GameConfiguration()
        self.__gameboard = Gameboard()
        self.__gameboard.setGameboard(self.__gameConfiguration)

        # self.connectConfigurationEvents()

    # def connectConfigurationEvents(self):
        # self.__gameConfiguration.getManualButton().clicked.connect(self.manualButtonClicked)
        # self.__gameConfiguration.getSolverButton().clicked.connect(self.solverButtonClicked)

    def manualButtonClicked(self):
        self.__gameboard.setGameboard(self.__gameConfiguration)

    def solverButtonClicked(self):
        print("solverButtonClicked")

    def getGameConfiguration(self):
        return self.__gameConfiguration

    def getGameboard(self):
        return self.__gameboard

    __gameConfiguration = None
    __gameboard = None

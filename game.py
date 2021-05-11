from game_configuration import GameConfiguration
from gameboard import Gameboard
from solver import Solver

class Game():
    def __init__(self):
        super(Game, self).__init__()

    def set(self):
        self.__gameConfiguration = GameConfiguration()
        self.__gameboard = Gameboard()
        self.__gameboard.setGameboard(self.__gameConfiguration)
        self.__solver = Solver(self)

        # self.connectConfigurationEvents()

    # def connectConfigurationEvents(self):
        # self.__gameConfiguration.getManualButton().clicked.connect(self.manualButtonClicked)
        # self.__gameConfiguration.getSolverButton().clicked.connect(self.solverButtonClicked)

    def manualButtonClicked(self):
        self.__gameboard.setGameboard(self.__gameConfiguration)

    def solverButtonClicked(self):
        """run solver"""
        self.__solver.set()
        self.__solver.run()

    def getGameConfiguration(self) -> GameConfiguration:
        return self.__gameConfiguration

    def getGameboard(self) -> Gameboard:
        return self.__gameboard

    __gameConfiguration = None
    __gameboard = None

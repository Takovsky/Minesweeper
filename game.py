from game_configuration import GameConfiguration
from gameboard import Gameboard
from solver import Solver
from randomSolver import RandomSolver
from logger import Logger

class Game():
    def __init__(self):
        super(Game, self).__init__()
        self.__logger = Logger()

    def set(self):
        self.__gameConfiguration = GameConfiguration()
        self.__gameboard = Gameboard()
        self.__gameboard.setGameboard(self.__gameConfiguration)
        self.__solver = Solver(self)
        self.__randomSolver = RandomSolver(self)

        # self.connectConfigurationEvents()

    # def connectConfigurationEvents(self):
        # self.__gameConfiguration.getManualButton().clicked.connect(self.manualButtonClicked)
        # self.__gameConfiguration.getSolverButton().clicked.connect(self.solverButtonClicked)

    def manualButtonClicked(self):
        self.__gameboard.setGameboard(self.__gameConfiguration)

    def solverButtonClicked(self, runs):
        """run solver"""
        self.prepareFileName("solver")
        self.__logger.createFile(self.__fileName)
        self.__logger.writeToFile(self.__fileName, self.getInitLog(True))

        for i in range(runs):
            self.__solver.set()
            self.__solver.run()
            self.__logger.writeToFile(self.__fileName, self.__solver.getResult())

    def randomButtonClicked(self, runs):
        """run random"""
        self.prepareFileName("random")
        self.__logger.createFile(self.__fileName)
        self.__logger.writeToFile(self.__fileName, self.getInitLog())

        for i in range(runs):
            self.__randomSolver.set()
            self.__randomSolver.run()
            self.__logger.writeToFile(self.__fileName, self.__randomSolver.getResult())

    def getGameConfiguration(self) -> GameConfiguration:
        return self.__gameConfiguration

    def getGameboard(self) -> Gameboard:
        return self.__gameboard

    def getLogger(self) -> Logger:
        return self.__logger

    def prepareFileName(self, solverType):
        separator = "_"
        extention = ".csv"
        
        self.__fileName = (solverType + separator + 
        str(self.__gameConfiguration.getSize()) + separator + 
        str(self.__gameConfiguration.getMines()) + separator + 
        str(self.__gameConfiguration.getRuns())) + extention

    def getInitLog(self, solver = False):
        separator = ";"
        newLine = "\n"

        firstLine = ("RUNS" + separator +  str(self.__gameConfiguration.getRuns()) + separator +
        "MINES" + separator + str(self.__gameConfiguration.getMines()) + separator +
        "SIZE" + separator  + str(self.__gameConfiguration.getSize()))

        secondLine = "MOVES" + separator + "WON"

        if solver:
            secondLine += separator + "FINISHED" + separator + "COMPLETEMENT"

        return firstLine + newLine + secondLine + newLine

    def isWon(self):
        return self.__gameboard.getGameWon()

    __gameConfiguration = None
    __gameboard = None
    __logger = None
    __fileName = None
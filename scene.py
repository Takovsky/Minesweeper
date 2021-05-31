from game import Game
from solver import Solver
from window import Window

class Scene():
    def __init__(self):
        super(Scene, self).__init__()

    def setScene(self):
        self.setGame()
        self.setWindow()
        self.connectEvents()

    def setGame(self):
        self.__game = Game()
        self.__game.set()

    def setWindow(self):
        self.__window = Window()
        self.__window.set(self.__game)

    def showScene(self):
        self.__window.show()

    def connectEvents(self):
        ## @todo: solver button connection has to be made either here or in game
        self.__game.getGameConfiguration().getManualButton().clicked.connect(self.manualButtonClicked)
        self.__game.getGameConfiguration().getSolverButton().clicked.connect(self.solverButtonClicked)
        self.__game.getGameConfiguration().getRandomButton().clicked.connect(self.randomButtonClicked)

    def manualButtonClicked(self):
        self.__game.manualButtonClicked()
        self.__window.resizeWindow(self.__game.getGameConfiguration())

    def solverButtonClicked(self):
        self.__game.solverButtonClicked(self.__game.getGameConfiguration().getRuns())
        self.__window.resizeWindow(self.__game.getGameConfiguration())

    def randomButtonClicked(self):
        self.__game.randomButtonClicked(self.__game.getGameConfiguration().getRuns())
        self.__window.resizeWindow(self.__game.getGameConfiguration())


    __game = None
    __solver = None
    __window = None

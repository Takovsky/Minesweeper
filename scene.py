from game import Game
from solver import Solver
from window import Window

class Scene():
    def __init__(self):
        super(Scene, self).__init__()

    def setScene(self):
        self.setGame()
        # self.setSolver()
        self.setWindow()
        self.connectEvents()

    def setGame(self):
        self.__game = Game()
        self.__game.set()

    def setSolver(self):
        self.__solver = Solver()
        # self.solver.set()

    def setWindow(self):
        self.__window = Window()
        self.__window.set(self.__game)

    def showScene(self):
        self.__window.show()

    def connectEvents(self):
        self.__game.getGameConfiguration().getManualButton().clicked.connect(self.manualButtonClicked)

    def manualButtonClicked(self):
        self.__game.manualButtonClicked()
        self.__window.resizeWindow(self.__game.getGameConfiguration())

    __game = None
    __solver = None
    __window = None

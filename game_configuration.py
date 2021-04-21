from PySide2.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, QPushButton
from single_game_configuration import SingleGameConfiguration

class GameConfiguration(QWidget):
    def __init__(self):
        super(GameConfiguration, self).__init__()
        self.initWidgets()
        self.initLayout()

    def initWidgets(self):
        self.__minesConfiguration = SingleGameConfiguration("mines", 10)
        self.__sizeConfiguration = SingleGameConfiguration("board size", 9)
        self.__solverConfiguration = SingleGameConfiguration("solver duration [s]", 2)
        self.initButtons()

    def initButtons(self):
        self.__manualButton = QPushButton(self)
        self.__manualButton.setText("Manual")
        self.__solverButton = QPushButton(self)
        self.__solverButton.setText("Solver")

    def initLayout(self):
        self.__layout = QGridLayout(self)
        self.__layout.addWidget(self.__minesConfiguration, 0, 0)
        self.__layout.addWidget(self.__sizeConfiguration, 0, 1)
        self.__layout.addWidget(self.__solverConfiguration, 0, 2)
        self.__layout.addWidget(self.__manualButton, 1, 0)
        self.__layout.addWidget(self.__solverButton, 1, 2)

    def getMines(self):
        return self.__minesConfiguration.get()

    def getSize(self):
        return self.__sizeConfiguration.get()

    def getManualButton(self):
        return self.__manualButton
    
    def getSolverButton(self):
        return self.__solverButton

    __layout = None
    __minesConfiguration = None
    __sizeConfiguration = None
    __solverConfiguration = None
    __manualButton = None
    __solverButton = None

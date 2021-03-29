from PySide2.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, QPushButton
from single_game_configuration import SingleGameConfiguration

class GameConfiguration(QWidget):
    def __init__(self):
        super(GameConfiguration, self).__init__()
        self.initWidgets()
        self.initLayout()

    def initWidgets(self):
        self.minesConfiguration = SingleGameConfiguration("mines", 10)
        self.sizeConfiguration = SingleGameConfiguration("board size", 10)

    def initLayout(self):
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.minesConfiguration, 0, 0)
        self.layout.addWidget(self.sizeConfiguration, 0, 1)

    def getMines(self):
        return self.minesConfiguration.get()

    def getSize(self):
        return self.sizeConfiguration.get()
    
    layout = None
    minesConfiguration = None
    sizeConfiguration = None
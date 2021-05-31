from PySide2.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, QPushButton


class SingleGameConfiguration(QWidget):
    def __init__(self, text, amount):
        super(SingleGameConfiguration, self).__init__()
        self.amount = amount
        self.initWidgets(text, amount)
        self.initLayout()

    def initWidgets(self, text, amount):
        self.__label = QLabel()
        self.__label.setText(text + ":")
        
        self.__lineEdit = QLineEdit()
        self.__lineEdit.setText(str(amount))

    def initLayout(self):
        self.__layout = QGridLayout(self)
        self.__layout.addWidget(self.__label, 0, 0)
        self.__layout.addWidget(self.__lineEdit, 0, 1)

    def get(self):
        return int(self.__lineEdit.text())

    __layout = None
    __label = None
    __lineEdit = None

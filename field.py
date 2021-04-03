from PySide2.QtWidgets import QWidget, QPushButton

class Field(QPushButton):
    def __init__(self):
        super(Field, self).__init__()
        self.setCheckable(True)
        self.setFixedSize(25, 25)
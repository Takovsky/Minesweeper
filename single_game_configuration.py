from PySide2.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, QPushButton


class SingleGameConfiguration(QWidget):
    def __init__(self, text, amount):
        super(SingleGameConfiguration, self).__init__()
        self.initWidgets(text, amount)
        self.initLayout()

    def initWidgets(self, text, amount):
        self.label = QLabel()
        self.label.setText(text + ":")
        self.label.setFixedSize(50, 20)
        
        self.lineEdit = QLineEdit()
        self.lineEdit.setText(str(amount))
        self.lineEdit.setFixedSize(50, 20)

        self.button = QPushButton()
        self.button.setText("Save")
        self.button.setFixedSize(50, 20)

    def initLayout(self):
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.lineEdit, 0, 1)
        self.layout.addWidget(self.button, 0, 2)

    def get(self):
        return int(self.lineEdit.text())

    layout = None
    label = None
    lineEdit = None
    button = None

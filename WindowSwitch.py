import sys
from PyQt5 import QtCore, QtWidgets
from FlashCardScreen import *

class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        layout = QtWidgets.QGridLayout()
        self.button = QtWidgets.QPushButton('Start Learning!')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit()

class Controller:

    def __init__(self):
        pass

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.showFlashCardScreen)
        self.window.show()
    
    def showFlashCardScreen(self):
        self.flashCardScreen = FlashCardScreen()
        self.window.close()
        self.flashCardScreen.switch_window.connect(self.showFlashCardScreen)
        self.flashCardScreen.show()

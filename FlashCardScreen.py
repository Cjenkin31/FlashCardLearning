import sys
from PyQt5 import QtCore, QtWidgets
from FlashCardReader import *
from correctIncorrect import *
import random

class FlashCardScreen(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Flash Cards')

        layout = QtWidgets.QGridLayout()
        quizzedWord = random.choice(list(TermDefDict().keys()))
        self.label = QtWidgets.QLabel(quizzedWord)
        layout.addWidget(self.label)

        self.userTextBoxAnswer = QtWidgets.QLineEdit()
        layout.addWidget(self.userTextBoxAnswer)

        self.submitAnswerButton = QtWidgets.QPushButton('Submit Answer')
        self.submitAnswerButton.clicked.connect(self.CheckAnswer)
        layout.addWidget(self.submitAnswerButton)

        self.setLayout(layout)

    def CheckAnswer(self):
        self.alert = QtWidgets.QMessageBox()
        fixedUserAnswer=self.userTextBoxAnswer.text().lower().encode('utf-8')
        fixedActualAnswer=TermDefDict()[self.label.text()].lower().encode('utf-8')
        stringedActualAnswer = str(fixedActualAnswer)[2:-1]
        if (fixedUserAnswer == fixedActualAnswer):
            self.alert.setText('Correct!')
        else:
            self.alert.setText('Incorrect! the answer was: ' + stringedActualAnswer)
        self.alert.exec()
        self.switch_window.emit()
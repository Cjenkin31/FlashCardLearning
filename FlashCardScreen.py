import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from PyQt5 import QtCore, QtWidgets
from FlashCardReader import *
from correctIncorrect import *
import random
from CorrectAnswerMaker import *
import keyboard as kb

class FlashCardScreen(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str,str,str)
    def __init__(self):
        
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Flash Cards')
        correctAnswerDict = ReadCorrectAnswers()
        listOfWeights = list(correctAnswerDict.values())

        layout = QtWidgets.QGridLayout()
        quizzedWord = random.choices(list(TermDefDict().keys()),weights=listOfWeights,k=1)
        self.label = QtWidgets.QLabel(quizzedWord[0])
        layout.addWidget(self.label)

        self.userTextBoxAnswer = QtWidgets.QLineEdit()
        layout.addWidget(self.userTextBoxAnswer)

        self.submitAnswerButton = QtWidgets.QPushButton('Submit Answer')
        self.submitAnswerButton.clicked.connect(self.CheckAnswer)
        layout.addWidget(self.submitAnswerButton)

        self.resetWeightsButton = QtWidgets.QPushButton('Reset Weights')
        self.resetWeightsButton.clicked.connect(self.Reset)
        layout.addWidget(self.resetWeightsButton)
        self.shortCutlabel = QtWidgets.QLabel("Ctrl+O to quickly enter")
        layout.addWidget(self.shortCutlabel)
        self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_open.activated.connect(self.CheckAnswer)
        self.setLayout(layout)

    def Reset(self):
        self.alert = QtWidgets.QMessageBox()
        ResetWeights()
        self.alert.setText('Weights have been reset')
        self.alert.exec()

    def CheckAnswer(self):
        self.switch_window.emit(self.userTextBoxAnswer.text().lower(),TermDefDict()[self.label.text()].lower(),self.label.text())
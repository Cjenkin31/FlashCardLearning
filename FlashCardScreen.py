import sys
from PyQt5 import QtCore, QtWidgets
from FlashCardReader import *
from correctIncorrect import *
import random
from CorrectAnswerMaker import *
class FlashCardScreen(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Flash Cards')
        correctAnswerDict = ReadCorrectAnswers()
        listOfWeights = list(correctAnswerDict.values())

        layout = QtWidgets.QGridLayout()
        # quizzedWord = random.choice(list(TermDefDict().keys()))
        quizzedWord = random.choices(list(TermDefDict().keys()),weights=listOfWeights,k=1)
        self.label = QtWidgets.QLabel(quizzedWord[0])
        layout.addWidget(self.label)

        self.userTextBoxAnswer = QtWidgets.QLineEdit()
        layout.addWidget(self.userTextBoxAnswer)

        self.submitAnswerButton = QtWidgets.QPushButton('Submit Answer')
        self.submitAnswerButton.clicked.connect(self.CheckAnswer)
        layout.addWidget(self.submitAnswerButton)

        self.submitAnswerButton = QtWidgets.QPushButton('Reset Weights')
        self.submitAnswerButton.clicked.connect(self.Reset)
        layout.addWidget(self.submitAnswerButton)

        self.setLayout(layout)

    def CheckAnswer(self):
        self.alert = QtWidgets.QMessageBox()
        fixedUserAnswer=self.userTextBoxAnswer.text().lower().encode('utf-8')
        fixedActualAnswer=TermDefDict()[self.label.text()].lower().encode('utf-8')
        stringedActualAnswer = str(fixedActualAnswer)[2:-1]
        correctAnswerDict = ReadCorrectAnswers()
        if (fixedUserAnswer == fixedActualAnswer):
            self.alert.setText('Correct!')
            correctAnswerDict[self.label.text()]=(.9)*float(correctAnswerDict[self.label.text()]) 
        else:
            self.alert.setText('Incorrect! the answer was: ' + stringedActualAnswer)
            correctAnswerDict[self.label.text()]=(1.1)*float(correctAnswerDict[self.label.text()])
        UpdateCorrectAnswers(correctAnswerDict)

        self.alert.exec()
        self.switch_window.emit()
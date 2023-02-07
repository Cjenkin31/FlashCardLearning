from PyQt5 import QtCore, QtWidgets
from FlashCardReader import *
from correctIncorrect import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from CorrectAnswerMaker import *
from WordTracker import *
class AnswerScreen(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, text, correctAnswer,definition):

        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Answer Screen')
        layout = QtWidgets.QGridLayout()
        weights = ReadCorrectAnswers()
        if (text.encode('UTF-8') == correctAnswer.encode('UTF-8')):
            self.label = QtWidgets.QLabel("Correct!")
            weights[definition]=weights[definition]*0.9
        else:
            self.label = QtWidgets.QLabel("Incorrect! the correct answer is: " + str(correctAnswer))
        layout.addWidget(self.label)
        
        self.correctLabelDef = QtWidgets.QLabel(definition)
        layout.addWidget(self.correctLabelDef)

        self.UserCorrectButton = QtWidgets.QPushButton('I was right!')
        self.UserCorrectButton.clicked.connect(self.UserCorrect)
        layout.addWidget(self.UserCorrectButton)

        self.nextCardButton = QtWidgets.QPushButton('Next Card')
        self.nextCardButton.clicked.connect(self.NextCard)
        layout.addWidget(self.nextCardButton)

        self.shortCutlabel = QtWidgets.QLabel("Ctrl+I I was Correct!, Ctrl+O next card")
        layout.addWidget(self.shortCutlabel)
        self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_open.activated.connect(self.NextCard)
        self.shortcut_openI = QShortcut(QKeySequence('Ctrl+I'), self)
        self.shortcut_openI.activated.connect(self.UserCorrect)

        self.setLayout(layout)

    def NextCard(self):
        weights = ReadCorrectAnswers()
        if (self.label.text() == "Correct!"):
            weights[self.correctLabelDef.text()]=weights[self.correctLabelDef.text()]*.9
            AddCorrect(self.correctLabelDef.text())
        else:
            weights[self.correctLabelDef.text()]=weights[self.correctLabelDef.text()]*1.1
            SubtractCorrect(self.correctLabelDef.text())
        UpdateCorrectAnswers(weights)
        self.switch_window.emit()
    def UserCorrect(self):
        weights = ReadCorrectAnswers()
        weights[self.correctLabelDef.text()]=weights[self.correctLabelDef.text()]*.9
        UpdateCorrectAnswers(weights)
        print(self.correctLabelDef.text())
        AddCorrect(self.correctLabelDef.text())
        self.switch_window.emit()
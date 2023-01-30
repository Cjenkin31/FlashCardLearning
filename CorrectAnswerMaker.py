import pickle

def ReadCorrectAnswers():
    correctAnswerDict = {}
    try:
        correctAnswerDict = pickle.load(open("correct.pickle", "rb"))
    except (OSError, IOError) as e:
        allCards = pickle.load(open("dict.pickle", "rb"))
        for card in allCards:
            correctAnswerDict[card] = 1.0
        pickle.dump(correctAnswerDict, open("correct.pickle", "wb"))
    return(correctAnswerDict)

def UpdateCorrectAnswers(correctAnswerDict):
    try:
        pickle.dump(correctAnswerDict, open("correct.pickle", "wb"))
        return True
    except (OSError, IOError) as e:
        return False

def ResetWeights():
    correctAnswerDict = {}
    allCards = pickle.load(open("dict.pickle", "rb"))
    for card in allCards:
        correctAnswerDict[card] = 1.0
    pickle.dump(correctAnswerDict, open("correct.pickle", "wb"))
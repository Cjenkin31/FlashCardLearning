import pickle

def ReadCorrectAnswers():
    correctAnswerDict = {}
    try:
        correctAnswerDict = pickle.load(open("pickle\correct.pickle", "rb"))
    except (OSError, IOError) as e:
        allCards = pickle.load(open("pickle/dict.pickle", "rb"))
        for card in allCards:
            correctAnswerDict[card] = 1.0
        pickle.dump(correctAnswerDict, open("pickle\correct.pickle", "wb"))
    return(correctAnswerDict)

def UpdateCorrectAnswers(correctAnswerDict):
    try:
        pickle.dump(correctAnswerDict, open("pickle\correct.pickle", "wb"))
        return True
    except (OSError, IOError) as e:
        return False

def ResetWeights():
    correctAnswerDict = {}
    allCards = pickle.load(open("pickle/dict.pickle", "rb"))
    for card in allCards:
        correctAnswerDict[card] = 1.0
    pickle.dump(correctAnswerDict, open("pickle\correct.pickle", "wb"))
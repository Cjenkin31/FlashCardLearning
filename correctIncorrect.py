import pickle

def IncorrectList():
    try:
        incorrectWords = pickle.load(open("pickle/incorrect.pickle", "rb"))
        if (incorrectWords.count < 1):
            raise Exception("no incorrect words found")
    except (OSError, IOError) as e:
        pickle.dump(incorrectWords, open("pickle/incorrect.pickle", "wb"))
        return []
    return( incorrectWords )

def CorrectList():
    try:
        correctWords = pickle.load(open("pickle\correct.pickle", "rb"))
        if (correctWords.count < 1):
            raise Exception("no correct words found")
    except (OSError, IOError) as e:
        pickle.dump(correctWords, open("pickle\correct.pickle", "wb"))
        return []
    return( correctWords )
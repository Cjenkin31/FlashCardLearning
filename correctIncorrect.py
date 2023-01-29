import pickle
import bz2
import os

def IncorrectList():
    try:
        incorrectWords = pickle.load(open("incorrect.pickle", "rb"))
        if (incorrectWords.count < 1):
            raise Exception("no incorrect words found")
    except (OSError, IOError) as e:
        pickle.dump(incorrectWords, open("incorrect.pickle", "wb"))
        return []
    return( incorrectWords )

def CorrectList():
    try:
        correctWords = pickle.load(open("correct.pickle", "rb"))
        if (correctWords.count < 1):
            raise Exception("no correct words found")
    except (OSError, IOError) as e:
        pickle.dump(correctWords, open("correct.pickle", "wb"))
        return []
    return( correctWords )
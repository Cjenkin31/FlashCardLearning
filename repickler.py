import pickle
import bz2
import codecs
import unicodedata as ud

def RePickle():
    f = codecs.open("allCards", "r", "utf-8")
    listOfCards = f.read().split("\n")
    f.close()
    termsDefin={}
    for card in listOfCards:
        wholeCard = card[:-1].split(",")
        termsDefin[wholeCard[0]] = wholeCard[1]
    pickle.dump(termsDefin, open("pickle/dict.pickle", "wb"))
    return(termsDefin)
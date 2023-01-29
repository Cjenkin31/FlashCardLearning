import pickle
import bz2

def TermDefDict():
    termsDefin = {}
    try:
        termsDefin = pickle.load(open("dict.pickle", "rb"))
    except (OSError, IOError) as e:
        with open(r"allCards", 'r') as cardFile:
            for line in cardFile:
                x = line[:-1]
                termsDefin[x.split(',')[0]] = x.split(',')[1]
        pickle.dump(termsDefin, open("dict.pickle", "wb"))
    return(termsDefin)
import pickle
import codecs

def TermDefDict():
    termsDefin = {}
    try:
        return pickle.load(open("pickle\dict.pickle", "rb"))
    except (OSError, IOError) as e:
        print("__________________")
        print("__________________")
        print(e)
        print("__________________")
        print("__________________")
        with codecs.open("allCards", "r", "utf-8") as cardFile:
            for line in cardFile:
                print(line)
                print((line[:-1])[2:-1])
                x = line[:-1].encode('utf-8')[2:-1]
                print(x)
                termsDefin[x.split(',')[0]] = x.split(',')[1]
        pickle.dump(termsDefin, open("pickle\dict.pickle", "wb"))
        return termsDefin
import random
from FlashCardReader import *
from CorrectAnswerMaker import *
def GetTenWords():
    tenWords = []
    try:
        tenWords = pickle.load(open("pickle/tested.pickle", "rb"))
    except (OSError, IOError) as e:
        tenWords = random.choices(list(TermDefDict().keys()),weights=ReadCorrectAnswers().values(),k=10)
        pickle.dump(tenWords, open("pickle/tested.pickle", "wb"))
    return(tenWords)

def SubtractCorrect(word):
    cntDict={}
    try:
        cntDict = pickle.load(open("pickle/correctRow.pickle", "rb"))
        print("___________________")
        print(word)
        print(cntDict)
        print("___________________")
        if word in cntDict and cntDict[word] != 0:
            cntDict[word]=cntDict[word]-1
        pickle.dump(cntDict, open("pickle/correctRow.pickle", "wb"))
    except (OSError, IOError) as e:
        for words in GetTenWords():
            cntDict[words]=0
        pickle.dump(cntDict, open("pickle/correctRow.pickle", "wb"))

def AddCorrect(word):
    cntDict={}
    try:
        cntDict = pickle.load(open("pickle/correctRow.pickle", "rb"))
        print(cntDict)
        print("The word is: " + word)
        if word in cntDict:
            cntDict[word] += 1
        else:
            cntDict[word] = 1
        if (cntDict[word]>=3):
            print("Adding New Word")
            AddNewWord(word)
            print("added")
            cntDict=GetCntDictionary()
            print(cntDict)
        pickle.dump(cntDict, open("pickle/correctRow.pickle", "wb"))
    except (OSError, IOError) as e:
        for words in GetTenWords():
            cntDict[words]=0
        pickle.dump(cntDict, open("pickle/correctRow.pickle", "wb"))

def RemoveCorrect(word):
    cntDict={}
    try:
        cntDict = pickle.load(open("pickle/correctRow.pickle", "rb"))
        if word in cntDict:
            del cntDict[word]
            pickle.dump(cntDict, open("pickle/correctRow.pickle", "wb"))
    except (OSError, IOError) as e:
        for words in GetTenWords():
            cntDict[words]=0
        pickle.dump(cntDict, open("pickle/correctRow.pickle", "wb"))
    return cntDict

def GetCntDictionary():
    cntDict={}
    try:
        cntDict = pickle.load(open("pickle/correctRow.pickle", "rb"))
    except (OSError, IOError) as e:
        GetTenWords()
    return cntDict

def AddNewWord(word):
    print("Getting the ten words...")
    testedWords = GetTenWords()
    print("Got the ten words...")
    for x in testedWords:
        if (x == word):
            print("Removing the word: "+word)
            testedWords.remove(word)
            print("Word Removed.")
            print("Removing the word from counter...")
            RemoveCorrect(word)
            print("Word removed from counter")
    print("Appending the word...")
    newChosenWord = random.choices(list(TermDefDict().keys()),weights=ReadCorrectAnswers().values(),k=1)[0]
    testedWords.append(str(newChosenWord))
    print("Word Appended: " + str(newChosenWord))
    pickle.dump(testedWords, open("pickle/tested.pickle", "wb"))
    print("Pickled new tested words: ")
    print(testedWords)
    return testedWords
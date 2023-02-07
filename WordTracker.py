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
        if (cntDict[word] != 0):
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
        cntDict[word]=cntDict[word]+1
        if (cntDict[word]>=3):
            print("Adding New Word")
            AddNewWord(word)
            print("added")
            cntDict=GetCntDictionary()
        pickle.dump(cntDict, open("pickle/correctRow.pickle", "wb"))
    except (OSError, IOError) as e:
        for words in GetTenWords():
            cntDict[words]=0
        pickle.dump(cntDict, open("pickle/correctRow.pickle", "wb"))

def RemoveCorrect(word):
    cntDict={}
    try:
        cntDict = pickle.load(open("pickle/correctRow.pickle", "rb"))
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
    testedWords = GetTenWords()
    for x in testedWords:
        if (x == word):
            testedWords.remove(word)
            RemoveCorrect(word)
        testedWords.append(random.choices(list(TermDefDict().keys()),weights=ReadCorrectAnswers().values(),k=1))
    pickle.dump(testedWords, open("pickle/tested.pickle", "wb"))
    return testedWords
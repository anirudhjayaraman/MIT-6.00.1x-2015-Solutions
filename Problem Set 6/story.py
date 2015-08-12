import string
import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):

    return random.choice(wordList)

def randomString(wordList, n):

    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):

    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():

    return open("story.txt", "r").read()



def buildCoder(shift):

    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase
    keys = lowerCase + upperCase
    shiftLower = ''
    shiftUpper = ''
    for i in range(26):
        index = (i + shift) % 26
        shiftLower += lowerCase[index]
        shiftUpper += upperCase[index]
    values = shiftLower + shiftUpper
    return dict(zip(keys, values))

def applyCoder(text, coder):

    coderDictionary = coder
    mapped = ''
    for i in text:
        
        if i in string.punctuation or i == ' ' or i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or i == '\n':
            mapped += i
        else:
            mapped += coderDictionary[i]
    return mapped
    
def applyShift(text, shift):

    return applyCoder(text, buildCoder(shift))
    
def findBestShift(wordList, text):

    realWords = 0
    bestShift = 0
    for possibleShift in range(26):
        sentence = applyShift(text, possibleShift)
        sentenceWords = sentence.split(' ')
        validWords = 0
        for word in sentenceWords:
            if isWord(wordList, word):
                validWords += 1
        if validWords > realWords:
            bestShift = possibleShift
            realWords = validWords
    return bestShift
    
    
    
def decryptStory():

    story = getStoryString()
    wordList = loadWords()
    shift = findBestShift(wordList, story)
    for i in range(26):
        print applyShift(story, i)
    return shift

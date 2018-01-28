import random
import string

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"

def loadWords():

    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList



def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,
    print

def isValidWord(word, hand, wordList):
    word1=list(word)
    hand1=[]
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand1.append(letter)
    word2=word1[:]
    if word in wordList:
        for e in word2:
            if e in hand1:
                word1.remove(e)
                hand1.remove(e)
        if len(word1)==0:
            return True
    else:
        return False

def getWordScore(word, n):
    score=0
    word1=list(word)
    for e in word1:
        score = score+SCRABBLE_LETTER_VALUES[e]
    score=score*len(word1)
    if len(word)==n:
        score=score+50
    return score

def updateHand(hand, word):
    word1=list(word)
    hand2=hand.copy()
    for e in word1:
        if e in hand2:
            hand2[e]=hand2.get(e)-1
    return hand2
    print(hand2)

wordList= loadWords()
n=2
hand={'a': 1, 'z': 1}
Total=0
hand1=hand.copy()

for letter in hand1:
    hand2=[]
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand2.append(letter)
for i in range(len(hand2)):
    if len(hand2)!=0:
        print('Current Hand:'),displayHand(hand1)
        word=str(raw_input('Enter a word, or a "." to indicate that you are finished: ')) 
        dot='.'
        if word==dot:
            print('Goodbye! Total score: '+str(Total)+' points')
            break
        else:
            Bin=isValidWord(word,hand,wordList)
            if Bin==True:
                Total=Total+(getWordScore(word,n))
                print('"'+word+'" earned '+str(getWordScore(word,n))+' points. Total: '+str(Total)+' points')
                hand1=updateHand(hand1,word)
                hand2=[]
                for letter in hand1.keys():
                    for j in range(hand1[letter]):
                        hand2.append(letter)
                print(' ')
        if Bin==False:
            print('Invalid word,please try again.')
            print(' ') 
else:
    print('Run out of letters. Total score: '+str(Total)+' points')
    
   
    
    
    
        

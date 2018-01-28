import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    secret=[]
    for s in range(len(secretWord)):
        secret.append(secretWord[s])
        secret1=secret[:]
    for e in secret:
        if e in lettersGuessed:
            secret1.remove(e)
    if len(secret1)==0:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    secret=[]
    for s in range(len(secretWord)):
        secret.append(secretWord[s])
        secret1=secret[:]
    Str=''
    for e in secret:
        if e in lettersGuessed:
            Str=Str+e
        else:
            Str=Str+' _ '
    return Str
    
def getAvailableLetters(lettersGuessed):
    alph=[]
    for s in range(len(string.ascii_lowercase)):
        alph.append((string.ascii_lowercase)[s])
        alph1=alph[:]
    for e in alph:
        if e in lettersGuessed:
            alph1.remove(e)
    alph2=''
    for e in alph1:
        alph2=alph2+e
    return alph2
    
def hangman(secretWord):
    import string
        
    print('Welcome to the game Hangman! ')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    print('-----------')
    guess=8
    lettersGuessed=[]
    secret=[]
    Str2=[]
    alph2=string.ascii_lowercase
    check = 0
    while guess>0 and check == 0:
        print('You have '+str(guess)+' guesses left')
        print('Available letters: '+ alph2)
        letter=str(raw_input('Please guess a letter: '))
        letter=letter.lower()
        alph4=[]
        for s in range(len(alph2)):
            alph4.append(alph2[s])
        lettersGuessed.append(letter[0])
        Str=getGuessedWord(secretWord,lettersGuessed)
        if letter not in alph4:
            print("Oops! You've already guessed that letter: "+Str)
            print('-----------')
            guess=guess
        else:
            Bool=isWordGuessed(secretWord,lettersGuessed)
            if letter in alph4:
                alph2=getAvailableLetters(lettersGuessed)
            for s in range(len(secretWord)):
                secret.append(secretWord[s])
            if letter in secret:
                print('Good guess: '+Str)
                print('-----------')
                guess=guess
            else:
                print('Oops! That letter is not in my word: '+Str)
                alph3=len(alph2)
                guess=guess-1
                print('-----------')
            Str2=[]
            for s in range(len(Str)):
                Str2.append(Str[s])
            Str3=Str2[:]
            underscore='_'
        if underscore in Str3:
            check=0
            if guess==0:
                print('Sorry, you ran out of guesses. The word was '+secretWord+'.')
        else:
            check = 1
            print('Congratulations, you won!')
    

wordlist = loadWords()
secretWord=random.choice(wordlist)
hangman(secretWord)
   

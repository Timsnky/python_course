import string
from ps5_encryption import *

def buildCoder(shift):
    alph=string.ascii_lowercase
    alph2=string.ascii_uppercase
    alph3=list(alph)
    alph4=list(alph2)
    alph5={}
    for e in range(len(alph4)):
        alph5[alph4[e]]=alph4[e+shift-26]
    for i in range(len(alph3)):
        alph5[alph3[i]]=alph3[i+shift-26]
    return alph5

def applyCoder(text,coder):
    text2=list(text)
    text3=''
    for e in range(len(text2)):
        if text2[e] in coder.keys():
            text2[e]=coder[text2[e]]
    for i in range(len(text2)):
        text3=text3+text2[i]
    return(text3)

def applyShift(text,shift):
    coder=buildCoder(shift)
    return(applyCoder(text,coder))

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList


text='Pmttw, ewztl!'
text2=list(text.split())
message=''
digits=list(string.digits)
punct=list(string.punctuation)
for k in range(len(text2)):
    if k==0:
        shift=0
    else:
        shift=shift
    print text2
    while 26-shift>0:
        print(shift)
        text5=''
        text3=list(text2[k])
        print text3
        text4=text3[:]
        for e in text4:
            if e in digits or e in punct:
                text3.remove(e)
        print text3
        print text4
        for e in text3:
            text5=text5+e
        print(text5)
        result=applyShift(text5,shift)
        print(result)
        result2=list(result)
        print(result2)
        if result in wordList:
            print(shift)
            for i in range(len(text4)):
                if text4[i] in digits or text4[i] in punct:
                    message=message+text4[i]
                
                else:
                    message=message+result2[i]
            message=message+' '
            print(message)
            break
        else:
            shift=shift+1
        
        

            
            
        
            
            
    
            
            
        

    







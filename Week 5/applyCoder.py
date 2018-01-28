import string
from cesar import *

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

wordList = loadWords()
text="Ftq fqmoTqd'e zmyq uE FMnuftM?"
def findBestSift(wordList,text):
    text2=list(text.split())
    message=''
    for k in range(len(text2)):
        if k==0:
            shift=0
        else:
            shift=shift
        while 26-shift>0:
            text5=''
            text3=list(text2[k])
            for e in text3:
                text5=text5+e
            result=applyShift(text5,shift)
            result2=list(result)
            if k==0:
                test=isWord(wordList,result)
                if test==True:
                    message=message+result
                    message=message+' '
                    break
                else:
                    shift=shift+1
            else:
                message=message+result
                message=message+' '
                break
    return shift
        
        

            
            
        
            
            
    
            
            
        

    







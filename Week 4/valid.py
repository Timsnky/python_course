wordList=['cup','frog','dog','cow','rapture']
word='rapture'
hand={'a':2,'c':1,'f':1,'r':1,'g':1,'o':3,'u':1,'e':1,'p':1}

def isValidWord(word,hand,wordList):
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
    else:
        return False

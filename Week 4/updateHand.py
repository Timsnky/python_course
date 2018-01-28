def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,
    print
    
def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
    
def updateHand(hand,word):
    word1=list(word)
    hand1=[]
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand1.append(letter)
    hand2=hand1[:]
    for e in word1:
        if e in hand2:
            hand1.remove(e)
    hand1=getFrequencyDict(hand1)
    return hand1
    print(hand1)

def updateHand2(hand,word):
    word1=list(word)
    hand2=hand.copy()
    for e in word1:
        if e in hand2:
            hand2[e]=hand2.get(e)-1
    return hand2
    print(hand2)
    

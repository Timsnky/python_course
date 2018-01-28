hand={'a':2,'b':1,'c':3,'d':1}
print(hand)
Total=0
hand1=hand.copy()
print(hand)
hand3=hand.copy()
for letter in hand1:
    hand2=[]
    for letter in hand3.keys():
        for j in range(hand[letter]):
            hand2.append(letter)
hand3=tuple(hand2)
print hand3

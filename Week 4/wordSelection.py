import random

n=int(raw_input('Enter n: '))
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
hand={}
numVowels=n/3

for i in range(numVowels):
    x=VOWELS[random.randrange(0,len(VOWELS))]
    hand[x]=hand.get(x,0)+1
for i in range(n/3,n):
    x=CONSONANTS[random.randrange(0,len(CONSONANTS))]
    hand[x]=hand.get(x,0)+1
print(hand)

def calculateHandlen(hand):
    length=0
    for e in hand:
        length=length+hand[e]
    return length

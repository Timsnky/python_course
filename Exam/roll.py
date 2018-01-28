import random

def probTest1(limit):
    numTries=0
    for i in range(10000):
        prob=1.0
        while prob > limit:
            roll=random.choice([1,2,3,4,5,6])
            numTries+=1
            if roll==1:
                prob=prob*(1.0/6.0)
                break
            else:
                prob=prob*(5.0/6.0)
    return (numTries/10000)

def probTest(limit):
    fail=5.0/6.0
    Pass=1.0/6.0
    roll=1
    while limit<((fail**(roll-1))*Pass):
        roll+=1
    return roll

print probTest(0.1)

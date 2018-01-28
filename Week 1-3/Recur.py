def recurPower1(base,exp):
    if exp==0:
        return 1
    else:
        return base* recurPower1(base,exp-1)

def iterPower(base,exp):
    ans=1
    while exp!=0:
        ans=ans*base
        exp-=1
    return ans

def recurPower(base,exp):
    if exp==0:
        return 1
    elif exp==1:
        return base
    else:
        if exp%2==1:
            return base* recurPower(base,exp-1)
        elif exp%2==0:
            return recurPower(base**2,exp/2)

def gcdIter(a,b):
    ans=min(a,b)
    while ans>0:
        if a%ans==0 and b%ans==0:
            break
        else:
            ans-=1
    return ans

def gcdRecur(a,b):
    c=min(a,b)
    d=max(a,b)
    if c==0:
        return d
    else:
        return gcdRecur(c,d%c)

def lenIter(aStr):
    ans=0
    for i in aStr:
        ans=ans+1
    return ans

def lenRecur(aStr):
    if aStr=='':
        return 0
    else:
        return 1+lenRecur(aStr[0:-1])
def isIn(char,aStr):
    if len(aStr)==0:
        return False
    else:
        low=aStr[0]
        high=aStr[-1]
        mid=aStr[(len(aStr))/2]
        if mid==char:
            return True
        else:
            if min(char,mid)==char:
                return isIn(char,aStr[0:(len(aStr))/2])
            else:
                return isIn(char,aStr[(len(aStr))/2+1:])
    


c=lenRecur('Timothy')
print c

def square(x):
    '''
    x: int or float.
    '''
    return x**2

def evalQuadratic(a, b, c, x):

    return (a*(x**2))+(b*x)+c

def clip(lo,x,hi):
    if min(lo,x)==x:
        return lo
    elif max(hi,x)==x:
        return hi
    else:
        return x

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(lo,x),hi)

def fourthPower(x):
    '''
    x: int or float.
    '''
    y=square(x)
    return square(y)

def odd(x):
    '''
    x: int or float.
    returns: True if x is odd, False otherwise
    '''
    return x%2!=0

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char=char.lower()
    if char=='a'or char=='e' or char=='i' or char=='o'or char=='u':
        return True
    else:
        return False

def isVowel2(char):
    '''
    char: a single letter of any case
    returns: True if char is a vowel and False otherwise.
    '''
    char=char.lower() 
    vowel='aeiou'
    return char in vowel

c=isVowel('A')
print c



    

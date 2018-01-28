def isWordGuessed(secretWord,lettersGuessed):
    secret=[]
    for s in range(len(secretWord)):
        secret.append(secretWord[s])
        secret1=secret[:]
    for e in secret:
        if e in lettersGuessed:
            secret1.remove(e)
    if len(secret1)==0:
        return True
    else:
        return False

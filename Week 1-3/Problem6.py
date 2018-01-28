def getGuessedWord(secretWord,lettersGuessed):
    secret=[]
    for s in range(len(secretWord)):
        secret.append(secretWord[s])
        secret1=secret[:]
    Str=''
    for e in secret:
        if e in lettersGuessed:
            Str=Str+e
        else:
            Str=Str+' _ '
    return Str

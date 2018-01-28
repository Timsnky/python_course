def getAvailableLetters(lettersGuessed):
    import string

    alph=[]
    for s in range(len(string.ascii_lowercase)):
        alph.append((string.ascii_lowercase)[s])
        alph1=alph[:]
    for e in alph:
        if e in lettersGuessed:
            alph1.remove(e)
    alph2=''
    for e in alph1:
        alph2=alph2+e
    return alph2

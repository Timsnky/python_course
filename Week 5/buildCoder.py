def buildCoder(shift):
    import string
    alph=string.ascii_lowercase
    alph2=string.ascii_uppercase
    alph3=list(alph)
    alph4=list(alph2)
    alph5={}
    for e in range(len(alph4)):
        alph5[alph4[e]]=alph4[e+Shift-26]
    for i in range(len(alph3)):
        alph5[alph3[i]]=alph3[i+Shift-26]
    return alph5





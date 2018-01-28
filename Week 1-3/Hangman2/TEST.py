secretWord=str(raw_input('Please Enter the Secret Word : '))
secret=[]
lettersGuessed=list(raw_input('Please Guess the Letters : '))
for s in range(len(secretWord)):
    secret.append(secretWord[s])
secret1=secret[:]
for e in secret:
    if e in lettersGuessed:
        secret1.remove(e)
if len(secret1)==0:
    print True
else:
    print False
ans=str(secret1)
Str=''
for e in secret:
    if e in lettersGuessed:
        Str=Str+e
    else:
        Str=Str+' _ '
print(Str)

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






    
        

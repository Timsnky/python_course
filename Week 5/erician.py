def x_ian(x,word):
    i=0
    text3=''
    if len(word)==0:
        return ''
    if len(x)==0:
        return text3
    if word[i]==x[i]:
        text3=text3+word[i]+x_ian(x[i+1:len(x)],word[i+1:len(word)])
    else:
        text3=text3+x_ian(x[i:len(x)],word[i+1:len(word)])
    return text3
word='czarinas'
x='sarina'
c=x_ian(x,word)
print c

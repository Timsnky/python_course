def x_ian(x,word):
    def erician1(x,word):
        i=0
        text3=''
        if len(word)==0:
            return ''
        if len(x)==0:
            return text3
        if word[i]==x[i]:
            text3=text3+word[i]+erician1(x[i+1:len(x)],word[i+1:len(word)])
        else:
            text3=text3+erician1(x[i:len(x)],word[i+1:len(word)])
        return text3
    if erician1(x,word)==x:
        return True
    else:
        return False
    
text='czarinas'
text1='sarina'
c=x_ian(text1,text)
print c

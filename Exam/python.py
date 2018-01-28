def laceStrings(s1,s2):
    i=0
    if len(s1)==0 and len(s2)==0:
        return ''
    elif len(s1)==0:
        return s2
    elif len(s2)==0:
        return s1
    elif len(s1)==1 or len(s2)==1:
        return s1+s2
    else:
        return s1[i]+s2[i]+laceStrings(s1[i+1:len(s1)],s2[i+1:len(s2)])

s1='abcdef'
s2='jklmnopqrstuv'
def laceStrings(s1,s2):
    s3=''
    i=0
    for i in range(min(len(s1),len(s2))):
        s3=s3+s1[i]+s2[i]
        i=i+1
    if len(s1)>len(s2):
        s3=s3+s1[i:len(s1)]
    else:
        s3=s3+s2[i:len(s2)]
    return s3

def laceStringsRecur(s1,s2):
    def helpLaceStrings(s1,s2,out):
        if s1=='':
            return s2
        if s2=='':
            return s1
        else:
            return s1[0]+s2[0]+helpLaceStrings(s1[1:len(s1)],s2[1:len(s2)],'')
    return helpLaceStrings(s1,s2,'')
s3= laceStringsRecur(s1,s2)
print(s3)
    


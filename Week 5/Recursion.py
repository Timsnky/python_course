
def reverseString(aStr):
    string2=aStr
    i=0
    if len(string2)==0:
        return ''
    elif len(string2)==1:
        return string2[0]
    else:
        return(string2[len(string2)-1]+reverseString(string2[i+1:len(string2)-1])+string2[i])


aStr='abcdefghijkl'
string3=reverseString(aStr)
print(string3)
print(aStr)

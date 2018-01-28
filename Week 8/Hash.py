import string

def hashStr(Str):
    num=''
    for e in Str:
        num=num+str(ord(e))
    ans = int(num)%7
    return ans

print hashStr('Eric')

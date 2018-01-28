def insertNewlines(text, lineLength):
   typeText=''
   if len(text) < lineLength:
        return typeText+text
   else:
       ans=text[:text.find(' ', lineLength-1)]
       typeText=typeText+ans+("\n")
       return typeText+ insertNewlines(text[len(ans)+1:], lineLength)

text='While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.'
lineLength=15

def insertNewlines1(text, lineLength):
    length=len(text)
    if length==0 or length<=lineLength:
        return text
    else:
        for i in range(lineLength, length):
            if text[i]!=' ':
                return (text[0:i]+'\n'+insertNewlines1(text[i+1:], lineLength))

c= insertNewlines(text,lineLength)
print(c)

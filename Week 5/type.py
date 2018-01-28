text='While I expect new intellectual adventures'
lineLength=15

def insertNewLines1(text,lineLength):
    def insertNewLines(text2,text3,lineLength):
               i=0
               if len(text2)==0:
                   return ''
               elif len(text3)>=15:
                   if text3[i]==' ':
                       return text3.append('\n')
                   else:
                       return text3.append(text2[i])
               else:
                   print(text3)
                   return text3.append(text2[i])+insertNewLines(text2[i+1:len(text2)],text3,lineLength)

    text2=list(text)
    text3=[]
    c=insertNewLines(text2,text3,lineLength)
    return c

c=insertNewLines1(text,lineLength)
print c
    
    




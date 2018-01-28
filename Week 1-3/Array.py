Elements=int(raw_input('Enter the Number of Elements: '))
i=0
Marks=[]
Sum=0
while i!=Elements:
    Num=int(raw_input('Enter marks number '))
    Marks.append(Num)
    i=i+1
for i in range(len(Marks)):
    Num1=Marks[i-1]
    Sum=Sum+Num1
print('The List is '+str(Marks))
print('The Sum of the List elements is '+str(Sum))
print('The Average of the elements is +'+str(round((float(Sum)/float(len(Marks))),2)))
    
    

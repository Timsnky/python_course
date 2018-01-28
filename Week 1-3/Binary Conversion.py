x=int(raw_input('Enter the Number'))
y=''
if x<0:
    z=True
    x=abs(x)
else:
    z=False
if x==0:
    y='0'
while x>0:
    y= str(x%2)+ y
    x=x/2
if z:
    y='-'+y
print(y)

    


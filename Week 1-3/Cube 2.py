x=int(raw_input('Enter the Number'))
y=0
while(y**3 < abs(x)):
    y=y+1
if(y**3==abs(x)):
    if(x<0):
       y=-y        
       print('The Cuberoot of ' +  str(x)  +  ' is '  +  str(y))
    else:
        print('The Cuberoot of '  +  str(x) +  ' is '  +  str(y))
else:
    print(str(x)  +  ' is not a Perfect Cube ')
      

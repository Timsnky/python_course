num=float(raw_input('Enter the Number'))
power=0
if num%1==0:
    z=True
    if num<0:
        y=True
        num=abs(num)
    else:
        y=False
else:
    z=False
    while ((2**power)*num)%1!=0:
         power=power+1
         
    num=(2**power)*num
num=int(num)
ans=''
if num==0:
    ans='0'
while num>0:
    ans=str(num%2)+ans
    num=num/2
    print(ans)

if not z:
    for i in range(power-len(ans)):
        ans='0'+ans
    ans='.'+ans
if z:
    if y:
       ans ='-'+ans

print('The Binary Equivalent is '+ans)




    
    




    
          

    
    

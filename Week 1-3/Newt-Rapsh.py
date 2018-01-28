x=float(raw_input('Enter the Number'))
approx=0.01
guess=0
ans=x/2.0
while abs(ans**2-x)>approx:
    ans=ans-(((ans**2)-x)/(2*ans))
    guess=guess+1
print(guess)
print('The approximate Square Root of '+str(x)+' is '+str(ans))



x=float(raw_input('Enter the Number'))
approx=0.01
step=approx**2
guess=0
ans=0
while (abs(ans**2-x))>approx and ans<x:
    ans=ans+step
    guess=guess+1
print('Guesses = '+str(guess))

if ans>=x:
    print('The Square root of '+str(x)+' could not be attained using the formular')
else:
    print('The approximate Square root is '+str(ans))


    

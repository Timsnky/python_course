x=float(raw_input('Enter the Number'))
approx=0.01
high=x
guess=0
low=0.0
ans=((high+low)/2.0)
while abs(ans**2-x)>approx:
    guess=guess+1
    if ans**2>x:
        high=ans
    else:
        low=ans
    ans=((high+low)/2.0)
print('Guesses= '+str(guess))
print('The Square Root of '+str(x)+' is '+str(ans))
    

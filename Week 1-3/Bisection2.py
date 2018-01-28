x=float(raw_input('Enter the Number'))
power= int(raw_input('Enter the power'))
def Rootfinder (x,approx,power,guess,high,low):
    ans=((high+low)/2.0)
    while abs((ans**power)-x)>approx:
         guess=guess+1
         if ans**power>x:
           high=ans
         else:
           low=ans
         ans=((high+low)/2.0)
    print('Guesses= '+str(guess))
    print('The '+str(power)+'th-root of '+str(x)+' is '+str(ans))
approx=0.01
guess=0
high=max(0,x)
low=min(0,x)

if x<0:
   if power%2==0:
      print('An even power doesnt have a negative')
   else:
       if x%1!=1:
           high=max(-1,x)
           low=min(-1,x)
           Rootfinder(x,approx,power,guess,high,low)
       else:
           Rootfinder(x,approx,power,guess,high,low)
else:
    if x%1!=1:
           high=max(1,x)
           low=min(1,x)
           Rootfinder(x,approx,power,guess,high,low)
    else:
        Rootfinder(x,approx,power,guess,high,low)

import pylab

def funct():
    i=-10
    epsilon=0.5
    y=[]
    while i<=10:
        y.append(i**3)
        i=i+epsilon
    return y

def funct2():
    i=-10
    epsilon=0.5
    x=[]
    while i<=10:
        x.append(i)
        i=i+epsilon
    return x

pylab.figure(1)
pylab.plot(funct2(),funct())
pylab.title('A Graph of the function y=x^3')
pylab.xlabel('x cordinates')
pylab.ylabel('y cordinates')
pylab.show()

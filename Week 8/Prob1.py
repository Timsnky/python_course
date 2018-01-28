import random
import pylab

def rand(numTries):
    num=''
    for i in range(numTries):
        num=num+str(random.choice([1,2,3,4,5,6]))
    return num

def randRoll(goal):
    numTries= len(goal)
    numRolls=0
    while True:
        result=rand(numTries)
        if result==goal:
            break;
        else:
            numRolls+=1
    return numRolls

def prob(goal,numChecks):
    total=0
    for i in range(numChecks):
        total=total+randRoll(goal)
    average=float(total/numChecks)
    return 'Probability = ',1/average

def rand1():
    return random.choice([1,2,3,4,5,6])

def checkPascal():
    tries=0.0
    for i in range(1):
        for j in range(1):
            roll1=rand1()
            roll2=rand1()
            if roll1==6 and roll2==6:
                tries+=1
                break
    return 1-(tries/10000)

def flip(trials):
    for j in range (trials):
        head=0
        for i in range(1000000):
            if random.random()<0.5:
                head+=1
        print head/float(1000000)
            
def plot(minflip,maxflip):
    ratio=[]
    diff=[]
    xaxis=[]
    for exp in range(minflip,maxflip+1):
        xaxis.append(2**exp)
    for flips in xaxis:
        head=0.0
        for e in range(flips):
            if random.random()<0.5:
                head+=1
        tails=flips-head
        differ=head-tails
        ratio.append(head/float(tails))
        diff.append(abs(differ))
    pylab.title('Difference Between Heada and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Difference')
    pylab.plot(xaxis,diff)
    pylab.figure()
    pylab.title('Ration between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Ratio')
    pylab.plot(xaxis,ratio)

##random.seed(0)
##plot(4,20)
##pylab.show()

def flu():
    flu_list=[]
    for y in range(12):
        if random.random()<0.1:
            flucatch=True
        else:
            flucatch=False
        flu_list.append(flucatch)
    return flu_list
        

def flu1(trials):
    yes=0.0
    for e in range(trials):
        k=0
        fluList=flu()
        for i in range(len(fluList)):
            if fluList[i]==True:
                k+=1
        if flu()[8]==True and flu()[9]==True and flu()[10]==True:
            yes+=1
    return yes

def flu2(trials):
    yes=0.0
    for e in range(trials):
        k=0
        fluList=flu()
        for i in range(len(fluList)):
            if fluList[i]==True:
                k+=1
        if flu()[8]==True and flu()[9]==False and flu()[10]==True:
            yes+=1
    return yes

def flu3(trials):
    yes=0.0
    for e in range(trials):
        k=0
        fluList=flu()
        for i in range(len(fluList)):
            if fluList[i]==True:
                k+=1
        if flu()[8]==True or flu()[9]==True or flu()[10]==True:
            yes+=1
    return yes

def flu4(trials):
    yes=0.0
    for e in range(trials):
        k=0
        fluList=flu()
        for i in range(len(fluList)):
            if fluList[i]==True:
                k+=1
        if (flu()[8]==True and flu()[9]==True)\
           or (flu()[8]==True and flu()[10]==True)\
           or (flu()[9]==True and flu()[10]==True)\
           or (flu()[8]==True and flu()[9]==True and flu()[10]==True):
            yes+=1
    return yes

#for i in range(5):
#    print flu4(10000)


def hist():
    vals=[]
    for i in range (10000):
        vals.append(random.random())
    xmin, xmax=pylab.xlim()
    ymin,ymax=pylab.ylim()
    print 'x-range=',xmin,'-',xmax
    print 'y-range=',ymin,'-',ymax
    pylab.hist(vals,11)

#hist()
#pylab.show()
    
def makenormal(mean,sd,numSamples):
    samples=[]
    for i in range(numSamples):
        samples.append(random.gauss(mean,sd))
    pylab.hist(samples,bins=101)

def makenormal2(mean,sd,numSamples):
    samples=[]
    for i in range(numSamples):
        samples.append(random.choice(range(1000)))
    pylab.hist(samples,bins=101)

##pylab.figure(1)
##makenormal(0.0,1.0,100000)
##pylab.figure(2)
##makenormal2(0.0,1.0,100000)
##pylab.show()

def drug(initial,prob,time):
    remnant=[initial]
    for e in range(time):
        remnant.append(initial*((1-prob)**e))
    pylab.plot(remnant,
               label = 'Exponential Decay')


##drug(1000,0.01,500)

def drug2(initial,prob,time):
    remnant=[initial]
    for i in range(time):
        if i%100==0 and i!=0:
            numLeft=2*(remnant[-1])
        else:
            numLeft=remnant[-1]
        for e in range(remnant[-1]):
            if random.random() <= prob:
                numLeft-=1
        remnant.append(numLeft)
    pylab.plot(remnant,'ro',label = 'Simulation')

##drug2(1000,0.01,500)
##pylab.legend()
##pylab.show()

x=3
if x>4:
    print 'yes'
else:
    raise NameError




        
        

    
    
    
        
    

    




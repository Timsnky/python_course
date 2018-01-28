import random

class Location(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def move(self,deltaX,deltaY):
        return Location(self.x+deltaX,self.y+deltaY)
    def distFrom(self,other):
        ox=other.x
        oy=other.y
        xDist=self.x-ox
        yDist=self.y-oy
        return(xDist**2+yDist**2)**0.5
    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'

class Field(object):
    def __init__(self):
        self.drunks={}  
    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[drunk]=loc
        return self.drunks
    def moveDrunk(self,drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist,yDist=drunk.takeStep()
        currentlocation=self.drunks[drunk]
        self.drunks[drunk]=currentlocation.move(xDist,yDist)
    def getLoc(self,drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        else:
            return self.drunks[drunk]
            
class  Drunk(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'The Drunk is called '+ self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0.0,1.0),(1.0,1.0),(1.0,0.0),(0.0,0.0)]
        return random.choice(stepChoices)

def walk(f,d,numSteps):
    start=f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return (start.distFrom(f.getLoc(d)))

def simWalks(numSteps,numTrials):
    homer=UsualDrunk('Homer')
    origin=Location(0,0)
    distances=[]
    for t in range(numTrials):
        f=Field()
        f.addDrunk(homer,origin)
        distances.append(walk(f,homer,numTrials))
    return distances

def drunkTest(numTrials=20):
    for numSteps in [10,100,1000,10000]:
        distances=simWalks(numSteps,numTrials)
        print 'Random Walk of '+str(numSteps)+' steps'
        print 'Mean = ',sum(distances)/len(distances)
        print 'Max = ',max(distances),' Min = ',min(distances)
        

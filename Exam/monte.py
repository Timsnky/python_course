import random
def sampleQuizzes():
    grades=[]
    trial=0
    for i in range(10000):
        mid1=random.choice(range(50,81))
        mid2=random.choice(range(60,91))
        exam=random.choice(range(55,96))
        grade=(0.25*mid1)+(0.25*mid2)+(0.5*exam)
        grades.append(grade)        
##        if grade>=70 and grade<=75:
##            trial+=1
##    return trial/10000.0
    return grades
    
import pylab
def plotQuizzes():
    pylab.title('Distribution of Scores')
    pylab.ylabel('Number of Trials')
    pylab.xlabel('Final Score')
    pylab.hist(sampleQuizzes(),bins=7)
    pylab.show()

plotQuizzes()



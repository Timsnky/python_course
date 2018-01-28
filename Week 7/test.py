import math

class test(object):
    def __init__(self):
        self.clean=[]

    def cleaner (self,pos):
        if pos in self.clean:
            return self.clean
        else:
            return self.clean.append(pos)
    def ist (self,p):
        if p in self.clean:
            return True
        else:
            return False

    def __str__(self):
        return str(self.clean)


a={(0, 1): True, (1, 2): False, (3, 2): False, (0, 0): False, (3, 1): False, (3, 3): False, (3, 0): False, (2, 2): False, (1, 1): False, (1, 4): False, (0, 2): False, (2, 0): False, (1, 3): False, (2, 3): False, (2, 1): True, (0, 4): False, (2, 4): True, (0, 3): False, (3, 4): False, (1, 0): True}
e=0
for i in a.keys():
    if a[i]==True:
        e=e+1
print e
        
    

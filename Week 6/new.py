class new(object):
    def __init__(self):
        self.x=[]
        self.index=len(self.x)
    def __str__(self):
        return str(self.x)
    def add(self,i):
        if i in self.x:
            raise ValueError(str(i)+' already in set')
        else:
            self.x.append(i)
            self.index=len(self.x)
    def remove(self,e):
        try:
            self.x.remove(e)
        except:
            raise ValueError(str(e)+' not in set')
    def member(self,e):
        return e in self.x
    def sort(self,i):
        if i not in self.x:
            for e in range(self.index):
                if i in self.x:
                    break
                elif i<self.x[e]:
                    temp=self.x[e]
                    self.x[e]=i
                    self.x.append(temp)
                    self.index=len(self.x)
                




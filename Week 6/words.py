import string

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class WordTrigger(Trigger):
    def __init__(self,word):
        Trigger.__init__(self)
        self.word=word
    def isWordIn(self,text):
        text2=text.lower()
        text3=text2
        for e in string.punctuation:
            if e in text3:
                text2=text2.replace(e," ")
        text2=text2.split()
        if (self.word.lower()) in text2:
            return True
        else:
            return False

class TitleTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSummary())

class NotTrigger(Trigger):
    def __init__(self,T):
        self.T=T
    def evaluate(self,x):
        return not self.T.evaluate(x)

class AndTrigger(Trigger):
    def __init__(self,T1,T2):
        self.T1=T1
        self.T2=T2
    def evaluate(self,x):
        return self.T1.evaluate(x) and self.T2.evaluate(x)

class OrTrigger(Trigger):
    def __init__(self,T1,T2):
        self.T1=T1
        self.T2=T2
    def evaluate(self,x):
        return self.T1.evaluate(x) or self.T2.evaluate(x)
    
class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        Trigger.__init__(self)
        self.phrase=phrase
    def evaluate(self,story):
        if self.phrase in story.getTitle() or self.phrase in story.getSubject() or self.phrase in story.getSummary():
            return True
        else:
            return False

def filterStories(stories,triggerlist):
    stories1=[]
    for e in range(len(stories)):
        for i in range(len(triggerlist)):
            if triggerlist[i].evaluate(stories[e])== True:
                stories1.append(stories[e])
    return stories1
                       
                       
        
        
            

            
            
        
        
        
        
    
    
    

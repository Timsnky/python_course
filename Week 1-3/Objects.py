def Tuples(n1,n2):
    t1=()
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            t1=t1+(i,)
    return t1

def List(l1,l2):
    l1clone=l1
    for e in l1clone:
        if e in l2:
            l1.remove(e)
            

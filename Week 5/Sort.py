L=[15,2,59,1,78,32,42,74,5,123]
for i in range(len(L)-1):
    minindex=i
    minvalue=L[i]
    j=i+1
    while j<len(L):
        if L[j]<minvalue:
            minindex=j
            minvalue=L[j]
        j=j+1
    temp=L[i]
    L[i]=L[minindex]
    L[minindex]=temp
print(L)

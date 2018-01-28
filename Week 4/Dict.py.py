sequence='abgrtbarrrty'
sequence1=list(sequence)
Dict={}
print(sequence1)
for e in sequence1:
    Dict[e]=Dict.get(e,0)+1
print(Dict)
for e in Dict.keys():
    for i in range(Dict[e]):
        print e,
print        
        
    

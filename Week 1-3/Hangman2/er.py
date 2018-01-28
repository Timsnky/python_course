num=[2,4,6,8]
l=[]
for i in range(len(num)):
	if i==0:
		l.append(0)
	else:
		l.append(num[i]*i)
print(l)

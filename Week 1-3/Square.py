x=int(raw_input('Enter the Number'))
for y in range(0,x-1):
    if y**2==x:
        print('The Square Root of' + str(x) + 'is' + str(y))
        break
if y**2!=x:
    print(str(x) +' is not a Perfect Square')

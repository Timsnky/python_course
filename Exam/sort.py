def sort1(lst):
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True
            print lst
        iteration += 1
        print iteration

def sort2(lst):
    for iteration in range(len(lst)):
        print iteration
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
            print(lst)
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp
        print lst
    return lst    



def sortt(lst):
    for i in range(len(lst)-1):
        print i
        minindex=i
        minval=lst[i]
        j=i+1
        while j< len(lst):
            if lst[j] < minval:
                minIndex = j
                minval = lst[j]
            j=j+1
            print lst
        temp=lst[i]
        lst[i]=lst[minindex]
        lst[minindex]=temp
        print lst

def sort3(lst):
    k=1
    l=2
    m=3
    out = []
    for iteration in range(0,len(lst)):
        print iteration
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            print out
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                print k
                print out
                break
        if not inserted:
            out.append(new)
            print l
            print out
    return out


def sort4(lst):
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])
        print 'iter'
        print(lst)
        print front
        print back
        return unite(front, back)


lst=[45,12,32,89,4,120,8]
c=sort3(lst)





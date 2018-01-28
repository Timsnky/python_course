def McNuggets(n):
    a=0
    b=0
    c=0
    for a in range((n/6)+1):
        for b in range((n/9)+1):
            for c in range((n/20)+1):
                mug=a*6+b*9+c*20
                if mug==n:
                    break
            if mug==n:
                break
        if mug==n:
            break
    if mug==n:
        return True
    else:
        return False
def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit(x), 0.0001)


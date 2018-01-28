def square(x):
    return x*x

def sq(a):
    b=1
    def tryit(b):
        return b*b
    return square(tryit(a))

c=sq(5)
print(c)

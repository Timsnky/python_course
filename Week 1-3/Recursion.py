def Square(a):
    return a*a

def cube (a):
    return a*a*a

def Mult (a,b):
    ans=0
    while b!=0:
        ans+=a
        b-=1
    return ans

def Mult2(a,b):
    ans=0
    for i in range(b):
        ans=ans+a
        b=b-1
    return ans

def Mult3 (a,b):
    if b==1:
        return a
    else:
        return a + Mult3(a,b-1)
def Power (a,b):
    if b==1:
        return a
    return a* Power(a,b-1)

"Factorial"
"Iterative"

def Factorial(n):
    ans=1
    while n>1:
        ans=ans*n
        n=n-1
    return ans

"Recursive"
def Factorial2(n):
    if n==1:
        return n
    return n*Factorial2(n-1)

"Towers of Hanoi"

def Print (fro,to):
    print('Move from '+str(fro)+' to '+str(to))

def Motion (n,fro,to,spare):
    if n==1:
        Print(fro,to)
    else:
        Motion(n-1,fro,spare,to)
        Motion(1,fro,to,spare)
        Motion(n-1,to,spare,fro)

"Fibonacci"

def fib (x):
    assert type(x)==int and x>=0
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

"Palindromes"

def Palindrome(s):
    def String (s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans=ans+c
        return ans
    def Pal (s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and Pal(s[1:-1])
    return Pal(String(s))
    

def obj (l,f):
    for i in range(len(l)):
        l[i]=f(l[i])
    print(l)

def obj1 (l,x):
    for f in l:
       print(f(x))
    
    
    

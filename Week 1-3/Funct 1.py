def Square(x,y):
    x=x*x
    y=y*y
    z=x*y
    return z
def cube(x,y,z):
    ans = Square(x,y)*z
    return ans

Str3=['a','b']
underscore='_'
if underscore not in Str3:
            check=1
            print('Congratulations, you won!')
else:
    check = 0
    print(check)

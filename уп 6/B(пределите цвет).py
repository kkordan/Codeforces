import math
x,y=map(float,input().split())
a=x*x+y*y
b=math.ceil(math.sqrt(a))

if b * b == a:
    print('black')
else:
    if x * y < 0:
        b+=1
    if b % 2 == 0:
        print('white')
    else:
        print('black')
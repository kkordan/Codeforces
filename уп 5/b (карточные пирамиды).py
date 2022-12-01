import math

t=int(input())

for i in range(t):
    n=int(input())
    s=0
    while n>=2:
        x= ((math.sqrt((24*n)+1)/6) - (1/6)) + 0.0000001

        n= n - (math.floor(x)*(3*math.floor(x)+1)/2)

        s+=1
    print(s)
import math
a,b,c=map(int,input().split())
x=(a*c/b)-c

x=math.ceil(x)

print(int(x))
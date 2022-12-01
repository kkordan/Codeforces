import math
n,r = map(int,input().split())
print(r * math.sin(math.pi/n)/(1-math.sin(math.pi/n)))
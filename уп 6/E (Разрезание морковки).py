import math
n,h = map(int, input().split())

for i in range(1,n):
    a = math.sqrt(h*h/n*i);
    print(a)
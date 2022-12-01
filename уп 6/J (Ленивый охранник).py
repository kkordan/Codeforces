import math

n=int(input())
a = math.floor(math.sqrt(n))
p=0
if a * a >= n:
    p = 4 * a
elif a*(a+1) >= n:
    p = 4*a + 2
elif ((a+1)*(a+1)) >= n:
    p = 4 * a + 4
print(p)
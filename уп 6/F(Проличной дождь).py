import math

d, h, v, e = map(int, input().split())
x = v/((math.pi*(d**2))/4)

if x > e:
    a = h/(4*v/(math.pi*(d**2))-e)

    print('YES')
    print(a)
else:
    print('NO')
import math

t=int(input())
for i in range(t):
    q=input().split()
    n=int(q[0])

    q=int(q[1])
    k=math.sqrt(q)+10
    x=0

    while x<k:
        x=x+1
        if (x+(q+x)//(x+1))<=n:
            break

    if x<k or n == q:
        print('YES')
    else:
        print('NO')

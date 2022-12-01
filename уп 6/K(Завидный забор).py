t=int(input())
for i in range(t):
    a=int(input())
    n=360/(180-a)
    if int(n) == n:
        print('YES')
    else:
        print('NO')
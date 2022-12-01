t = int(input())
while t:
    r = 0
    c = int(input())

    a = list(map(int,input().split()))
    a.insert(0, 0)

    for i in range(c, 0, -1):
        if i+a[i]<=c:
            a[i]+=a[i+a[i]]
        r=max(r, a[i])
    print(r)
    t-= 1
t= int(input())
for i in range(t):
    a=[]
    n, m = map(int, input().split())
    for ii in range(n):
        a.append(list(map(int, input().split())))
    l = [0] * (n + m + 2)
    r = [0] * (n + m + 2)
    for ii in range(n):
        for iii in range(m):
            l[ii - iii] += a[ii][iii]
            r[ii + iii] += a[ii][iii]
    s = 0
    for ii in range(n):
        for iii in range(m):
            s = max(s, l[ii - iii] + r[ii + iii] - a[ii][iii])
    print(s)

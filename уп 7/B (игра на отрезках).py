import sys
t=int(input())
for p in range(t):
    n = int(input())
    a = []
    for k in range(n):
        x, y = map(int, input().split())
        a.append([y - x, x, y])
    a = sorted(a)
    x = []


    for s, l, r in a:
        i = l
        while i in x:
            i = i + 1
        x.append(i)
        print(l, r, i)
sys.exit()
t = int(input())
for i in range(t):
    k = list(map(int, input().split()))
    s = sum(k)
    s2 = 0
    print(min(k[1],min(k[0],s//3)))
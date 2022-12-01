t = int(input())

while t:
    n = int(input())
    a = []
    for i in range(0, n):
        k = input()
        a.append([])
        for j in range(0, n):
            a[i].append(int(k[j]))
    x = 1
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            if a[i][j] and not a[i + 1][j] and not a[i][j + 1]:
                x = 0
    print("YES" if x else "NO")
    t -= 1
t = int(input())
for i in range(t):
    su = 0
    su = input()
    s = 0
    ii = 0
    while ii <= len(su) // 2:
        if su[ii] != 'a':
            print("YES")
            print(su + "a")
            s += 1
            break
        if su[len(su) - ii - 1] != 'a':
            print("YES")
            print("a" + su)
            s += 1
            break
        ii += 1
    if s != 1:
        print("NO")
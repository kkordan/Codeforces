t = int(input())
for i in range(t):
    s = str(input())
    p=0
    while p != 1:
        if s != s[::-1]:
            print(s)
            p+=1
        elif s.count(s[0]) == len(s):
            print(-1)
            p += 1
        else:
            s = [s[i:i + 1] for i in range(0, len(s), 1)]
            s=sorted(s)
            s=''.join(s)

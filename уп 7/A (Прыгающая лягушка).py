t =int(input())
for i in range(t):
    s = str(input())
    a=0
    b=0
    s = 'R'+s+'R'
    for ii in range(len(s)):
        if s[ii] == 'R':
            b=max(b,ii-a)
            a = ii
    print(b)
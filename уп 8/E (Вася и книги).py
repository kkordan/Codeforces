t = int(input())
for i in range(t):
    n,x,y,d = map(int,input().split())
    otv = -1
    n-=1
    x-=1
    y-=1
    a = y - x
    if a <= 0:
        a = a * (-1)
    if (a % d) == 0:
        otv = a / d
    elif ((n % d) == 0) and ((y % d) == 0):
        aa = y/d + (x+d-1)/d
        bb = (n - x + d - 1) / d + (n - y) / d
        if aa < bb :
            otv = aa
        else:
            otv = bb
    elif y % d == 0:
        otv = y / d + (x + d - 1)/ d
    elif (n - y) % d == 0:
        otv = (n - x + d - 1) / d + (n - y) / d
    print(int(otv))






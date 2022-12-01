t = int(input())
for i in range(t):
    otv= 0
    ch = int(input())
    for ii in range(3, ch+1, 2 ):
        k = ii * ii
        b = (k - 1) / 2
        c = k - b
        if b > ch or c > ch:
            break
        otv +=1
    print(otv)
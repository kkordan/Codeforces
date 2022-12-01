n = int(input())

pd = list(map(int, input().split()))


for i1 in range(1,n+1):
    ii = 0
    while ii!= n:
        if i1 == pd[ii]:
            print (ii+1)
            break
        else:
            ii = ii+1


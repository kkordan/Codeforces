tt=int(input())
ml=[]
q=[]

t=True

for i in range(tt):
    l= list(map(int,input().split()))

    k=l[0]
    n = 0


    while t == True:
        n+=1

        if (k % l[n]) == 0:
            o = 0
            ml.append(o)
        elif (k-l[n])>0:
            i=1
            r = k // l[n]
            i = l[n]*(r+1)
            h = k - i
            o =h
            o =int(o)
            o =abs(o)
            ml.append(o)

        if (k - l[n]) < 0:
            o = k - l[n]
            o = abs(o)
            ml.append(o)

        if n == 3:
            break
    m=min(ml)
    q.append(m)
    ml = []


print(*q, sep='\n')
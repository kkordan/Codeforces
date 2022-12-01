t = int(input())
for i in range(t):
    x=int(input())
    if x >45:
        print(-1)
    else:
        a=[]
        if x<9 :
            n=x
        else:
            n=9

        while x>0 and n>0:
            if x >=n:
                x-=n
                a.insert(0,str(n))
            n-=1
        print(''.join(a))



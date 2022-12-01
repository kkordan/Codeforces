n,k=map(int,input().split())
i=1
s=0

while i<=n:
    s=s+i
    s1=s-k

    if(s1>=0) and (i+s1)==n:
        print(s1)
        break
    i=i+1
n,t=map(int,input().split())
m=100000000
bm=0
c=0
for i in range(1,n+1):
    s,d=map(int,input().split())
    if t>s :
        c=abs(((abs(s-t)) % d )- d) % d
    else:
        c=s-t
    if c<m:
        m=c
        bm=i
print(bm)




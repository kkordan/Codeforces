sk,n=map(int,input().split())
sd=[]
b=[]
ii=0
for i in range(n):
    a,c= map(int,input().split())
    sd.append(a)
    b.append(c)
s = list(zip(sd, b))
ss = sorted(s, key=lambda tup: tup[0])
for i in range(n):
    if ss[i][0]< sk:
        sk=sk + ss[i][1]
        ii+=1
    else:
        print('NO')
        break
    if ii == n:

        print('YES')

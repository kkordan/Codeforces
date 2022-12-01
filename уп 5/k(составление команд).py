t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a<b:
        s=a
    else:
        s=b
    if ((a+b)//4)<=s:
        s=(a+b)//4
    print(s)

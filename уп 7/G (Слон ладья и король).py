r1,c1,r2,c2=map(int,input().split())
a = 2
b=2

if r1 == r2 or c1 == c2:
    a = 1
if ((r1 + c1) % 2) != ((r2 +c2) % 2):
    b=0
elif (r1 +c1 == r2 + c2) or (r1 + c2 == r2 + c1):
    b=1

c = max(abs(r1 - r2),abs(c1 - c2))
print(a,b,c)



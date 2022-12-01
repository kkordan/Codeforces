n=int(input())
ax,ay=map(int,input().split())
bx,by=map(int,input().split())
cx,cy=map(int,input().split())
p = True
if ((bx < ax) and (ax < cx)) or ((cx < ax) and (ax < bx))or ((by < ay) and (ay < cy)) or ((cy < ay) and (ay < by)):
    p=False

print("YES" if p else "NO")

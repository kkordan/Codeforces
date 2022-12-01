import sys
n, h=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
prover = 0
if a[0]== 0:
    print("NO")
    sys.exit()

elif (a[h-1] == 1):
    print("YES")
    sys.exit()
else:
    for i in range(h, n):
        if a[i] == 1 and b[i] == 1 and b[h-1]==1:
            print("YES")
            sys.exit()
print("NO")
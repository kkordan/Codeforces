t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a1= a.copy()
    a1=list(set(a1))
    s1=len(a1)


    if (s1 == 1) and (n % 2 == 0):


        print(0)
    elif (s1 == 1) and (n % 2 != 0):
        print(1)

    else:
        if (n-s1)% 2 !=0:
            a1.pop(0)
        print(len(a1))

for t in range(int(input())):
    n = int(input())
    s = input()
    r = ''
    for i in s:
        if(i!='1'):
            r += str(int(i)//2)
        else:
            r +=  i +'0'*(n-len(r)-1)
            break
    r = int(r)
    r1 = int(s)-r
    print(r)
    print(r1)
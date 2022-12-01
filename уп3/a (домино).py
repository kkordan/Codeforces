a=int(input())
down=[]
sl={'L':'L','R':'R','D':'U','U':'D'}

for i in range(a):
    s = int(input())
    up=str(input())

    up = list(up)

    for ii in range(s):
        down.append(sl[up[ii]])

    print(''.join(down))
    down.clear()
    up.clear()
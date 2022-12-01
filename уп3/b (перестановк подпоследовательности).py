t = int(input())
for i in range(t):
    n = int(input())
    slovo = str(input())
    slovo_sort = list(slovo)
    slovo_c = slovo_sort.copy()
    slovo_sort.sort()
    s=0
    for ii in range(n):
        if slovo_c[ii] != slovo_sort[ii]:
            s += 1
    print(s)
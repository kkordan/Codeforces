t = int(input())
a = []
for i in range(t):
    n = int(input())
    skob = input()
    s = 1

    while s != 0:
        if skob.count('()')> 0:
            skob = skob.replace('()', '')
        s = skob.count('()')
    e = skob.count('(')

    a.append(e)

print(*a, sep='\n')
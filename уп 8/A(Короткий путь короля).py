f = input()
j = input()

a = ord(f[0])
b = ord(f[1])
c = ord(j[0])
d = ord(j[1])
print(max(abs(a-c), abs(b-d)))
while a!=c or b!=d:
    if a < c:
        print("R", end = '')
        a+=1
    if a > c:
        print("L", end = '')
        a-=1
    if b > d:
        print("D", end = '')
        b-=1
    if b < d:
        print("U", end = '' )
        b+=1
    print()
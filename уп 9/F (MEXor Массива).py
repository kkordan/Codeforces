for i in range(int(input())):
    a, b = map(int, input().split())
    t = (a // 2) % 2
    if (a % 2):
        t ^= (a - 1)
    t ^= b
    if t == 0:
        print(a)
    elif t == a:
        print(a + 2)
    else:
        print(a + 1)

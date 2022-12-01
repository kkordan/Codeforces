t=int(input())
for i in range(t):
    x=int(input())
    print("YES" if x >= 111 * (x % 11) else "NO")
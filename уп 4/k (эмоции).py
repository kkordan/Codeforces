n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a =sorted(a, reverse=True)
p = m //(k+1)
h =a[0]-a[1]
s = a[0]*m-h*p
print(s)
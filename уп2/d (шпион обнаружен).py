t =int(input())
for i in range(t):
    n=int(input())
    pd = list(map(int, input().split()))
    print(int(*[pd.index(i) for i in pd if pd.count(i) == 1]) + 1)




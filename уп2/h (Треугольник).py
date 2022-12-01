pd = list(map(int, input().split()))

pd=sorted(pd)
if pd[0]+pd[1]>pd[2] or pd[1]+pd[2]>pd[3]:
    print('TRIANGLE')
elif pd[0]+pd[1]==pd[2] or pd[1]+pd[2]==pd[3]:
    print('SEGMENT')
else:
    print('IMPOSSIBLE')

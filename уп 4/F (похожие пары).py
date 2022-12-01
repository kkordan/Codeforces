t = int(input())


for i in range(t):

	n = int(input())
	a = [int(i) for i in input().split()]

	x = 0
	y = 0
	for ii in a:

		if ii % 2 == 0:
			x += 1

		else:
			y += 1
	if x % 2 == 0 and y % 2 == 0:

		print("YES")
	else:

		w = False
		for iii in a:
			if iii + 1 in a:
				w = True
		if w == True:

			print("YES")
		else:
			print("NO")
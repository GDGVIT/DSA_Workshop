for abc in range(int(input())):
	a, b = map(int, input().split())

	x = (a+b)/2
	y = (a-b)/2

	if (x != (a+b)//2) or (y != (a-b)//2) or x<0 or y<0:
		z.append("impossible")
	else:
		z.append(str((a+b)//2) + " " + str((a-b)//2))

for i in z:
	print(i)
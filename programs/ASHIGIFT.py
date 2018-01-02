number_of_test_cases = int(input())
final_results = [] # Will store the final result for each test case in a list

def f(initial, v):
	for item in v:
		if len(item)==2:
			initial -= item[1]
		elif initial>=item[1]:
			initial += item[2]

	return initial>0




for each_test_case in range(number_of_test_cases):
	X = int(input())
	B, *xy = map(int, input().split())

	final_xy = []
	best_case = 1
	for i in range(0,2*B,2):
		final_xy.append([xy[i], xy[i+1]])
		best_case += xy[i+1]

	C, *pqr = map(int, input().split())

	final_pqr = []
	for i in range(0, 3*C, 3):
		final_pqr.append([pqr[i], pqr[i+1], pqr[i+2]])

	final_vector = sorted(final_xy + final_pqr, key = lambda ele: (ele[0], -len(ele)))

	low = 1
	high = best_case

	possible_answer = best_case

	while (low<=high):
		mid = (low + high) // 2

		if (f(mid, final_vector)):
			possible_answer = min(possible_answer, mid)
			high = mid - 1
		else:
			low = mid + 1

	final_results.append(possible_answer)


for i in final_results:
	print(i)
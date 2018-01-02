number_of_test_cases = int(input())
final_results = [] # Will store the final result for each test case in a list

for each_test_case in range(number_of_test_cases):
	n,k = map(int, input().split())
	forgotten = input().split()
	modern = []

	for i in range(k):
		modern.extend(input().split())

	result = []
	for x in forgotten:
		flag = 0
		if x in modern:
			flag = 1
			result.append("YES")

		if not flag:
			result.append("NO")

	final_results.append(" ".join(result))

for i in final_results:
	print(i)
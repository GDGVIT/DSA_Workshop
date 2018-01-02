number_of_test_cases = int(input())
final_results = [] # Will store the final result for each test case in a list

for each_test_case in range(number_of_test_cases):
	p = int(input())
	result = 0
	for i in range(11, -1, -1):
		result += p // 2**i
		p = p % 2**i
		
	final_results.append(result)

for i in final_results:
	print(i)
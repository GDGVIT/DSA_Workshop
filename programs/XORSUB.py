number_of_test_cases = int(input())
final_results = [] # Will store the final result for each test case in a list

for each_test_case in range(number_of_test_cases):
	n,k = map(int, input().split())
	a = list(map(int, input().split()))

	dp = [0] * 1024

	dp[0] = 1

	for i in range(n):
		for j in range(1024):
			dp[j^a[i]] = dp[j^a[i]] or dp[j]

	ans = k

	for i in range(1024):
		if (dp[i]):
			ans = max(ans, k^i)

	final_results.append(ans)

for i in final_results:
	print(i)
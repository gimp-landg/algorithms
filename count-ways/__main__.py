# https://www.hackerrank.com/challenges/count-ways-1

N = int(raw_input())
A = [None] + map(int, raw_input().strip().split())
[L, R] = map(int, raw_input().strip().split())
M = 1000000007

def count_ways(N, A, L, R):
	cumulative_map = [None]
	for i in range(1, R+1):
		cumulative_map.append([0])
		for j in range(1, N+1):
			if A[j] < i:
				ij = cumulative_map[i][j-1] + cumulative_map[i-A[j]][j]
			elif A[j] > i:
				ij = cumulative_map[i][j-1]
			elif A[j] == i:
				ij = cumulative_map[i][j-1] + 1
			cumulative_map[i].append(ij % M)
	result = 0
	for f in cumulative_map[L: R+1]:
		result = (result + f[-1]) % M
	return result

print count_ways(N, A, L, R)

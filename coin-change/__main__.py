# submitted to hackerrank
# https://www.hackerrank.com/challenges/coin-change
def init(n, c):
	global WAYS_TABLE, N, C
	N = n
	C = c
	WAYS_TABLE = [{i:0 for i in C} for j in range(N+1)]
	for wt in WAYS_TABLE: wt.update({'calculated' : False})

def get_ways(i):
	if not WAYS_TABLE[i]['calculated']:
		for j in C:
			if j < i:
				WAYS_TABLE[i][j] = sum([get_ways(i-j)[k] for k in C if k<=j])
		if i in C:
			WAYS_TABLE[i][i] = 1
		WAYS_TABLE[i]['calculated'] = True
	return WAYS_TABLE[i]

if __name__ == '__main__':
	N, M = raw_input().strip().split(' ')
	N, M = [int(N), int(N)]
	C = map(int, raw_input().strip().split(' '))

	init(N, C)
	print sum([get_ways(N)[k] for k in C])

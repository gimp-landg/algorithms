# submitted to hackerrank
# https://www.hackerrank.com/challenges/coin-change
def init(c):
	global WAYS_TABLE, N, C
	C = c
	WAYS_TABLE = [{'calculated' : False}]

def get_ways(i):
	if len(WAYS_TABLE) - 1 < i:
		ways_columns = [{k:0 for k in C} for l in range(i - len(WAYS_TABLE) + 1)]
		for k in ways_columns: k.update({'calculated' : False})
		WAYS_TABLE.extend(ways_columns)

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

	init(C)
	print sum([get_ways(N)[k] for k in C])

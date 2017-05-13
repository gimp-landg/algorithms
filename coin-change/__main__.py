# submitted to hackerrank
# https://www.hackerrank.com/challenges/coin-change
def init(nl, Cl):
	global ways_table, n, C
	n = nl
	C = Cl
	ways_table = [{i:0 for i in C} for j in range(n+1)]
	for wt in ways_table: wt.update({'calculated' : False})

def get_ways(i):
	if not ways_table[i]['calculated']:
		for j in C:
			if j < i:
				ways_table[i][j] = sum([get_ways(i-j)[k] for k in C if k<=j])
		if i in C:
			ways_table[i][i] = 1
		ways_table[i]['calculated'] = True
	return ways_table[i]

if __name__ == '__main__':
	n, m = raw_input().strip().split(' ')
	n, m = [int(n), int(m)]
	C = map(int, raw_input().strip().split(' '))

	init(n, C)
	print sum([get_ways(n)[k] for k in C])

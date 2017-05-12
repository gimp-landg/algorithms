# submitted to hackerrank
# https://www.hackerrank.com/challenges/coin-change

def get_ways(i):
	if not ways_table[i]['calculated']:
		for j in C:
			if j < i:
				ways_table[i][j] = sum([get_ways(i-j)[k] for k in C if k<=j])
		if i in C:
			ways_table[i][i] = 1
		ways_table[i]['calculated'] = True
	return ways_table[i]
	
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
C = map(int, raw_input().strip().split(' '))
C.sort()
ways_table = [{i:0 for i in C} for j in range(n+1)]
for wt in ways_table: wt.update({'calculated' : False})

# Print the number of ways of making change for 'n' units using coins having the values given by 'C'
get_ways(n)
print sum([ways_table[n][k] for k in C])

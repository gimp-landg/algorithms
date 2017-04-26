# common-child challenge from
# https://www.hackerrank.com/challenges/common-child

def get_longest_common_child_length(a_string, b_string):
	a_set = set(a_string)
	b_set = set(b_string)
	a_preproc = ''.join([c for c in a_string if c in b_set])
	b_preproc = ''.join([c for c in b_string if c in a_set])

	return _get_longest_common_child_length(a_preproc, b_preproc)

def _get_longest_common_child_length(a_string, b_string):
	a_len = len(a_string) + 1
	b_len = len(b_string) + 1
	# longest common child length table as lcclt
	lcclt = [[0]*(b_len) for i in range(a_len)]
	for i in range(1, a_len):
		for j in range(1, b_len):
			if a_string[i-1] != b_string[j-1]:
				lcclt[i][j] = max(lcclt[i-1][j], lcclt[i][j-1])
			else:
				lcclt[i][j] = lcclt[i-1][j-1] + 1
	return lcclt[-1][-1]


if __name__ == '__main__':
	a_string = raw_input().strip()
	b_string = raw_input().strip()
	print get_longest_common_child_length(a_string, b_string)

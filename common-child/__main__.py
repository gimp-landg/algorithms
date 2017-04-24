# common-child challenge from
# https://www.hackerrank.com/challenges/common-child

def get_longest_common_child_length(a_string, b_string):
	a_set = set(a_string)
	b_set = set(b_string)
	a_preproc = ''.join([c for c in a_string if c in b_set])
	b_preproc = ''.join([c for c in b_string if c in a_set])

	_init_longest_common_child_length_map(a_preproc, b_preproc)

	return _get_longest_common_child_length(a_preproc, b_preproc)

def _init_longest_common_child_length_map(a_string, b_string):
	global longest_common_child_length_table
	a_len = len(a_string)+1
	b_len = len(b_string)+1
	longest_common_child_length_table = [[0]*b_len for i in range(a_len)]

def _get_longest_common_child_length(a_string, b_string):
	global longest_common_child_length_table
	lcclt = longest_common_child_length_table
	for i in range(1, len(a_string)+1):
		for j in range(1, len(b_string)+1):
			if a_string[i-1] != b_string[j-1]:
				lcclt[i][j] = max(lcclt[i-1][j], lcclt[i][j-1])
			else:
				lcclt[i][j] = lcclt[i-1][j-1] + 1
	return lcclt[len(a_string)][len(b_string)]


if __name__ == '__main__':
	a_string = raw_input().strip()
	b_string = raw_input().strip()
	print get_longest_common_child_length(a_string, b_string)

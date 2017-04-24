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
	global longest_common_child_length_map
	a_range = range(len(a_string)+1)
	b_range = range(len(b_string)+1)
	longest_common_child_length_map = {(a_string[0:i], b_string[0:j]) : 0 for i in a_range for j in b_range}

def _get_longest_common_child_length(a_string, b_string):
	global longest_common_child_length_map
	lcclm = longest_common_child_length_map
	for i in range(1, len(a_string)+1):
		for j in range(1, len(b_string)+1):
			if a_string[i-1] != b_string[j-1]:
				lcclm[(a_string[0:i], b_string[0:j])] = max(lcclm[(a_string[0:i-1], b_string[0:j])],
					lcclm[(a_string[0:i], b_string[0:j-1])])
			else:
				lcclm[(a_string[0:i], b_string[0:j])] = lcclm[(a_string[0:i-1], b_string[0:j-1])] + 1
	return lcclm[(a_string, b_string)]


if __name__ == '__main__':
	a_string = raw_input().strip()
	b_string = raw_input().strip()
	print get_longest_common_child_length(a_string, b_string)

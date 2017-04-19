# common-child challenge
# https://www.hackerrank.com/challenges/common-child

def get_longest_common_child_length(a_string, b_string):
	a_preproc = [c for c in a_string if c in b_string]
	b_preproc = [c for c in b_string if c in a_string]

	a_children = find_all_children(a_preproc)
	b_children = find_all_children(b_preproc)

	return max([len(w) for w in a_children & b_children])

def find_all_children(string):
	string_children =['']
	for c in string:
		string_children += [w+c for w in string_children]
	return set(string_children)

if __name__ == '__main__':
	a_string = raw_input().strip()
	b_string = raw_input().strip()
	print get_longest_common_child_length(a_string, b_string)

# common-child challenge
# https://www.hackerrank.com/challenges/common-child

def get_longest_common_child_length(a_string, b_string):
	a_set = set(a_string)
	b_set = set(b_string)
	a_preproc = [c for c in a_string if c in b_set]
	b_preproc = [c for c in b_string if c in a_set]

	common_children = find_all_children(a_preproc, b_preproc)

	return max([len(w) for w in common_children])

# input of find_all_children can be list as well as string
def find_all_children(a_string, b_string):
	children = set([''])
	for c in a_string:
		map(children.add, [w+c for w in children if is_child_of(w+c,b_string)])
	return children

def is_child_of(child, parent):
	child_len = len(child)
	if child_len <= len(parent):
		i=0
		cc = child[i]
		for pc in parent:
			if pc == cc:
				if i == child_len-1:
					return True
				else:
					i += 1
					cc = child[i]
		return False
	else:
		return False


if __name__ == '__main__':
	a_string = raw_input().strip()
	b_string = raw_input().strip()
	print get_longest_common_child_length(a_string, b_string)

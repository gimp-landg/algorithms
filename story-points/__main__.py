class OrderedTree:
	def __init__(self, key, val):
		# __tree = [key, left_node, right_node, linked_list_link]
		# __linked_list = [key, left_node, right_node, value]
		none_ll = [None, None, None, None]
		init_list = [key, None, None, val]
		init_list[1] = init_list[2] = none_ll
		none_ll[1] = none_ll[2] = init_list
		self.__linked_list = none_ll
		self.__tree = [key, None, None, self.__linked_list[2]]

	def add_key_value(self, key, value):
		self.__add_key_to_bt(key)[3] = self.__add_key_value_to_ll(key, value)

	def __add_key_to_bt(self, key, branch=None):
		if branch == None:
			branch = self.__tree

		if branch[0] == key:
			raise
		elif branch[0] > key:
			if branch[1] == None:
				branch[1] = [key, None, None, None]
				return branch[1]
			else:
				return self.__add_key_to_bt(key, branch=branch[1])
		elif branch[0] < key:
			if branch[2] == None:
				branch[2] = [key, None, None, None]
				return branch[2]
			else:
				return self.__add_key_to_bt(key, branch=branch[2])


	def __add_key_value_to_ll(self, key, value):
		node = self.__linked_list
		while True:
			if (node[0] == None or node[0] < key) and (node[2][0] > key or node[2][0] == None):
				a = node[2]
				node[2] = [key, node, a, value]
				a[1] = node[2]
				return node[2]
			elif node[0] == key:
				raise
			node = node[2]

	def get_values(self, *args):
		if len(args) == 1:
			return self.__get_values_from_key(*args)
		elif len(args) == 2:
			return self.__get_values_from_key_range(*args)
		else:
			raise

	def __get_values_from_key(self, key):
		left_range = None
		right_range = None
		branch = self.__tree
		while True:
			if branch is None:
				return [i[3] for i in left_range, right_range if i != None]
			elif branch[0] == key:
				return [branch[3]]
			elif branch[0] < key:
				left_range = branch
				branch = branch[2]
			elif branch[0] > key:
				right_range = branch
				branch = branch[1]


	def __get_values_from_key_range(self, key1, key2):
		if key1 > key2:
			key1, key2 = key2, key1
		node1 = self.__get_values_from_key(key1)[0]
		result = [node1]
		node = node1
		while node[0] < key2:
			node = node[2]
			if node[0] == None:
				return result
			result.append(node)
		return result


# create the data structure with story point data
ot = OrderedTree(4, '3 - 5 days')
for i in [(1, 'less than 1 day'), (16, '2 -5 weeks'), (0, '0 days'), (2, '1 - 2 days'), (8, '1 - 2 weeks'), (32, 'more than 5 weeks')]:
	ot.add_key_value(i[0], i[1])

# define a function that takes story points integer or range and prints information
def how_long(*points):
	for i in ot.get_values(*points):
		print i[0], ' : ', i[3]

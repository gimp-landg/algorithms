from ordered_tree import OrderedTree

# create the data structure with story point data
ot = OrderedTree(4, '3 - 5 days')
for i in [(1, 'less than 1 day'), (16, '2 -5 weeks'), (0, '0 days'), (2, '1 - 2 days'), (8, '1 - 2 weeks'), (32, 'more than 5 weeks')]:
	ot.add(i[0], i[1])

# define a function that takes story points integer or range and prints information
def how_long(*points):
	for i in ot.get_values(*points):
		print '{} : {}'.format(*i)

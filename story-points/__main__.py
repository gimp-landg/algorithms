from ordered_tree import OrderedTree
import argparse

# create the data structure with story point data
ot = OrderedTree(4, '3 - 5 days')
story_points_value_pairs = [
	(1, 'less than 1 day'),
	(16, '2 -5 weeks'),
	(0, '0 days'),
	(2, '1 - 2 days'),
	(8, '1 - 2 weeks'),
	(32, 'more than 5 weeks'),
]

for i in story_points_value_pairs:
	ot.add(i[0], i[1])

# define a function that takes story points integer or range (int1, int2)
# and prints the estimated time of accomplishment
def get_how_long(*points):
	for i in ot.get_values(*points):
		print '{} : {}'.format(*i)

# parse command line arguments
parser = argparse.ArgumentParser(description='Tool to display the value of agile story points.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer as the number of stroy points')

# pass the parsed arguments to the main function
args = parser.parse_args()
story_points = args.integers
story_points.sort()
get_how_long(story_points[0], story_points[-1])

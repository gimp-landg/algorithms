from quicksort import sort

def test(numbers):
	print numbers
	print sort(numbers)
	print ""

numbers = []
test(numbers)

numbers = [2]
test(numbers)

numbers = [9,2]
test(numbers)

numbers = [2,9]
test(numbers)

numbers = [66,2,9, 0]
test(numbers)

numbers = [66, 11, 2, 9, 77, 0]
test(numbers)

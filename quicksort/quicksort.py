from random import randint

def sort(v_numbers):
	global numbers, rec_stack
	numbers = v_numbers
	rec_stack = [(0,len(numbers)-1)]
	while len(rec_stack) > 0:
		_sort()
	return numbers

def _sort():
	i = rec_stack[-1][0]
	j = rec_stack[-1][1]
	del rec_stack[-1]
	if j - i < 1:
		return
	old_i = i
	old_j = j
	pivot = numbers[randint(i, j)]
	while j - i > 0:
		while numbers[i] < pivot and \
		      i <= old_j:
			i += 1
		while numbers[j] >= pivot and \
		      j >= old_i:
			j -= 1
		if i < j:
			numbers[i], numbers[j] = numbers[j], numbers[i]

	new_j = i
	new_i = j
	if j - i == 0:
		if numbers[j] >= pivot:
			new_i -= 1
		else:
			new_j += 1

	rec_stack.append((old_i, new_i))
	rec_stack.append((new_j, old_j))


from random import randint

def sort(v_numbers):
	global numbers
	numbers = v_numbers
	_sort(0,len(numbers)-1)
	return numbers

def _sort(i, j):
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
	_sort(old_i, new_i)
	_sort(new_j, old_j)


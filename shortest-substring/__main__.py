# Given a string S and a set of characters C,
# return the length of the shortest substring of S which contains all of C characters.

# S <- input string
# C <- input characters
S = raw_input().strip()
C = set(raw_input().strip())

C_index = { c : None for c in C }
min_len = None
enumerate_S = enumerate(S)
for i, c in enumerate_S:
	if c in C_index:
		C_index[c] = i
		if all([val != None for val in C_index.itervalues()]):
			min_len = max(C_index.values()) - min(C_index.values()) + 1
			break

for i, c in enumerate_S:
	if c in C_index:
		C_index[c] = i
		current_len = max(C_index.values()) - min(C_index.values()) + 1
		if current_len < min_len:
			min_len = current_len

if min_len != None:
	print min_len
else:
	print 'some of the characters cannot be found'

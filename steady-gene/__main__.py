def init():
    global nucleotides, nucleotide_len, left_count_map
    nucleotides = ['A', 'T', 'C', 'G']
    nucleotide_len = string_len/4
    left_count_map = [None for i in range(string_len+1)]
    left_count_map[0] = {key : 0 for key in nucleotides}

    for i, c in enumerate(string):
        left_count_map[i+1] = dict(left_count_map[i])
        left_count_map[i+1][c]+=1

def becomes_steady_gene(i,j):
    assert i<=j
    for c in nucleotides:
        if left_count_map[-1][c] + left_count_map[i][c] - left_count_map[j][c] > nucleotide_len:
            return False
    return True

def exists_steady_gene(length):
    for i in range(string_len+1-length):
        if becomes_steady_gene(i, i + length):
            return True
    return False

def min_steady_gene():
    a = 0
    b = 3 * string_len/4
    while True:
        if a == b:
            return a
        mid = (a+b)/2
        if exists_steady_gene(mid):
            b = mid
        else:
            a = mid + 1


if __name__ == '__main__':
    string_len = int(raw_input().strip())
    string = raw_input().strip()
    init()
    print min_steady_gene()

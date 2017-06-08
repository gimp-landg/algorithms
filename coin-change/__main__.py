# submitted to hackerrank
# https://www.hackerrank.com/challenges/coin-change
N, M = raw_input().strip().split(' ')
N, M = [int(N), int(M)]
C = map(int, raw_input().strip().split(' '))

from coin_changer_wrapper import sum_ways

print sum_ways(C, N)

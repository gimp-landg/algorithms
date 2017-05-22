# submitted to hackerrank
# https://www.hackerrank.com/challenges/coin-change
N, M = raw_input().strip().split(' ')
N, M = [int(N), int(N)]
C = map(int, raw_input().strip().split(' '))

from coin_changer import CoinChanger
cc = CoinChanger(C)
print cc.sum_ways(N)

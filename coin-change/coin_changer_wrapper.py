from coin_changer import CoinChanger

# todo garbage collector for coin_changers_map
coin_changers_map = {}

def sum_ways(C, N):
	C.sort()
	tC = tuple(C)
	if not tC in coin_changers_map:
		coin_changers_map[tC] = CoinChanger(C)

	return coin_changers_map[tC].sum_ways(N)

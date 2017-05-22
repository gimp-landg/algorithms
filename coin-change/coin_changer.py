class CoinChanger:
	def __init__(self, c):
		self.c = c
		self.ways_table = [{'calculated' : False}]

	def sum_ways(self, i):
		return sum([self._get_ways(i)[k] for k in self.c])

	def _get_ways(self, i):
		if len(self.ways_table) - 1 < i:
			ways_columns = [{k:0 for k in self.c} for l in range(i - len(self.ways_table) + 1)]
			for k in ways_columns: k.update({'calculated' : False})
			self.ways_table.extend(ways_columns)

		if not self.ways_table[i]['calculated']:
			for j in self.c:
				if j < i:
					self.ways_table[i][j] = sum([self._get_ways(i-j)[k] for k in self.c if k<=j])
			if i in self.c:
				self.ways_table[i][i] = 1
			self.ways_table[i]['calculated'] = True

		return self.ways_table[i]

from random import randint

# one card of the pack
class Card(object):
	def __init__(self, suit, value):
		assert suit in ['clubs', 'diamonds', 'hearts', 'spades']
		assert value in ['A'] + range(2, 11)+['J', 'Q', 'K']
		object.__setattr__(self, "suit", suit)
		object.__setattr__(self, "value", value)

	def __setattr__(self, *args):
		raise TypeError

	def __delattr__(self, *args):
		raise TypeError

# N packs of cards
class Cards:
	current_index = -1
	values = ['A'] + range(2, 11)+['J', 'Q', 'K']
	suits =  ['clubs', 'diamonds', 'hearts', 'spades']
	list = []
	def __init__(self, N):
		self.N = N
		for i in range(N):
			for suit in self.suits:
				for value in self.values:
					self.list.append(Card(suit, value));
		self.cards_number = 52*N

	def shuffle(self, times):
		for i in range(times):
			a = randint(0, self.cards_number/2)
			b = randint(self.cards_number/2+1, self.cards_number-1)
			self.list = self.list[0:a] + self.list[b:self.cards_number] + self.list[a:b]

	def match(self, mc_list, i):
		result = [getattr(self.list[i], mt) == getattr(self.list[i-1], mt) for mt in mc_list]
		return any(result)

# a player
class Player(object):
	def __init__(self):
		self.score = 0

	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self, score):
		assert isinstance(score, int) or isinstance(score, float)
		assert score >= 0
		self.__score = score

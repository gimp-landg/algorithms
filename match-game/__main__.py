# Simulate a card game called "match" between two computer players using N packs of cards.
# The cards being shuffled.
# Cards are revealed one by one from the top of the pile.
# The matching condition can be the face value of the card, the suit, or both.
# When two matching cards are played sequentially, a player is chosen randomly
# as having declared "match!" first and takes ownership of all the revealed cards.
# Game is continued until pile is exhausted.

from random import randint
from sys import exit
import lib

while True:
	try:
		N = int(raw_input('Type how many packs of cards to use (N): '))
		mc = int(raw_input('Choose matching condition (mc): type "1" for value, "2" for suit, "3" for both: '))
		break
	except ValueError:
		print('That was no valid number. Try again')

# create a pile using N (from input) pacs of cards
cards = lib.Cards(N)

# create two players
player1 = lib.Player()
player2 = lib.Player()

# shuffle the cards
cards.shuffle(cards.cards_number)

# define set of matching conditions
mc_list = ['value'] if mc == 1 else ['suit'] if mc ==2 else ['value', 'suit'] if mc ==3 else exit("%s is not acceptable value for matching condition" % mc)

# play the game
i = 1
while i < cards.cards_number:
	mc_value = cards.match(mc_list, i)
	if mc_value:
		score = i - cards.current_index

		# choose a player randomly as having declared "match!"
		if randint(0,1) == 0:
			player1.score += score
		else:
			player2.score += score

		# update current index for next match
		cards.current_index = i
		i += 1
	i += 1

# print the results of the game
print 'player1: %s cards' % player1.score
print 'player2: %s cards' % player2.score
winner = 'player1' if player1.score > player2.score else 'player2' if player1.score < player2.score else 'none'
print 'The winner is %s' % winner

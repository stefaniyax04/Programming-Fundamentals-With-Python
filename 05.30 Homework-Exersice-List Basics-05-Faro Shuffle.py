# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly
# in half. Then the cards in the two halves are perfectly interleaved, such that the original
# bottom card is still on the bottom and the original top card is still on top.
#
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives
# ['ace', 'four', 'two', 'five', 'three', 'six']
#
# Write a program that receives a single string (cards separated by space) and on the second line
# receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
#
# Note: The length of the deck of cards will always be an even number.

cards_input = input()
shuffle_count_input = input()

cards = cards_input.split()
shuffle_count = int(shuffle_count_input)

for _ in range(shuffle_count):
    half = len(cards) // 2
    left = cards[:half]
    right = cards[half:]
    shuffled = []
    for i in range(half):
        shuffled.append(left[i])
        shuffled.append(right[i])
    cards = shuffled

print(cards)
# Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of
# depression. And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain pokemon,
# those closest to you naturally get further, and those further from you, get closer.
# You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin
# receiving integers, which will correspond to indexes in that sequence.
# When you receive an index, you must remove the element at that index from the sequence (as if you've captured the
# pokemon).
# •	You must increase the value of all elements in the sequence that are less or equal to the removed element with
# the value of the removed element.
# •	You must decrease the value of all elements in the sequence that are greater than the removed element with the
# value of the removed element.
# If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
# If the given index is greater than the last index of the sequence, remove the last element from the sequence, and
# copy the first element to its place.
# The increasing and decreasing elements should also be done in these cases. The element whose value you should use
# is the removed element.
# The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).


distances = list(map(int, input().split()))
total_removed = 0

while distances:
    index = int(input())
    if index < 0:
        removed = distances.pop(0)
        if distances:
            distances.insert(0, distances[-1])
    elif index >= len(distances):
        removed = distances.pop(-1)
        if distances:
            distances.append(distances[0])
    else:
        removed = distances.pop(index)
    total_removed += removed
    for i in range(len(distances)):
        if distances[i] <= removed:
            distances[i] += removed
        else:
            distances[i] -= removed

print(total_removed)

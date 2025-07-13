# Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its
# innovative and unbelievably clever merging and dividing data into partitions. As the lead security developer
# in the CIA, you have been tasked to analyze the software of the virus and observe its actions on the data.
# You will receive a single input line containing strings, separated by spaces. The strings may contain any
# ASCII character except whitespace. Then you will begin receiving commands in one of the following formats:
# •	merge {startIndex} {endIndex}
# •	divide {index} {partitions}
# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex.
# In other words, you should concatenate them.
# Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
# Every time you receive the divide command, you must divide the element at the given index into several small
# substrings with equal length. The count of the substrings should be equal to the given partitions.
# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal
# lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1". At that point, you must print the resulting elements,
# joined by a space.
# Input
# •	The first input line will contain the array of data.
# •	On the next several input lines, you will receive commands in the format specified above.
# •	The input ends when you receive the command "3:1".

data = input().split()

while True:
    command = input()
    if command == "3:1":
        break

    parts = command.split()
    action = parts[0]

    if action == "merge":
        start = int(parts[1])
        end = int(parts[2])

        start = max(0, start)
        end = min(len(data) - 1, end)

        if start <= end:
            merged = ''.join(data[start:end + 1])
            data[start:end + 1] = [merged]

    elif action == "divide":
        index = int(parts[1])
        partitions = int(parts[2])

        element = data[index]
        length = len(element)

        part_length = length // partitions
        new_parts = []
        pos = 0

        for i in range(partitions - 1):
            new_parts.append(element[pos:pos + part_length])
            pos += part_length

        new_parts.append(element[pos:])

        data[index:index + 1] = new_parts

print(' '.join(data))

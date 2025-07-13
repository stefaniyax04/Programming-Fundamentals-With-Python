# You will be given two sequences of strings, separated by ", ". Print a new list containing only the
# strings from the first input line, which are substrings of any string in the second input line.

first = input().split(", ")
second = input().split(", ")

result = []

for word in first:
    for s in second:
        if word in s:
            result.append(word)
            break

print(result)

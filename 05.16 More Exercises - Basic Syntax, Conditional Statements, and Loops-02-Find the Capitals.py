# Write a program that takes a single string and prints a list of all the capital letters indice.

text = input()

indices = []
for i in range(len(text)):
    if text[i].isupper():
        indices.append(i)

print(indices)

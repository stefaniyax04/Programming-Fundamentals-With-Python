# On the first line, you will receive a number n. On the second line, you will receive a word.
# On the following n lines, you will be given some strings. You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

n = int(input("Enter number of elements: "))
word = input("Enter word: ")
list_1 = []
list_2 = []

for i in range(n):
    string = input("Enter string: ")
    list_1.append(string)

    if word in string:
        list_2.append(string)

print(list_1)
print(list_2)



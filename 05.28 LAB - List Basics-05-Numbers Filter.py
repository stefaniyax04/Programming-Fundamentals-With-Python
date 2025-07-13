# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input("Enter number of elements: "))

numbers = []
for i in range(n):
    number = int(input("Enter number: "))
    numbers.append(number)

command = input("Enter command: ")

if command == "even":
    result = [x for x in numbers if x % 2 == 0]
elif command == "odd":
    result = [x for x in numbers if x % 2 != 0]
elif command == "negative":
    result = [x for x in numbers if x < 0]
elif command == "positive":
    result = [x for x in numbers if x >= 0]

print(result)


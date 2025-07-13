# Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number
# n represents the count of numbers to remove from the list. You should remove the smallest ones, and then, you should
# print all the numbers that are left in the list, separated by a comma and a space ", ".

numbers_input = input()
n_input = input()

numbers = numbers_input.split()
n = int(n_input)

int_numbers = []
for item in numbers:
    int_numbers.append(int(item))

for _ in range(n):
    smallest = min(int_numbers)
    int_numbers.remove(smallest)

str_numbers = []
for item in int_numbers:
    str_numbers.append(str(item))

print(", ".join(str_numbers))


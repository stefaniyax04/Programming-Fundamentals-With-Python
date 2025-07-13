# Write a program that receives a sequence of numbers (a string containing integers
# separated by ", ") and prints the numbers sorted into lists of 10's in the format "Group of
# {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.

numbers = list(map(int, input().split(", ")))

groups = {}

min_group = ((min(numbers) - 1) // 10 + 1) * 10 if numbers else 10
max_group = ((max(numbers) - 1) // 10 + 1) * 10 if numbers else 10

for g in range(min_group, max_group + 10, 10):
    groups[g] = []

for num in numbers:
    group = ((num - 1) // 10 + 1) * 10
    groups[group].append(num)

for group in sorted(groups):
    print(f"Group of {group}'s: {groups[group]}")

# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

numbers = list(map(int, input().split(", ")))
even_indices = [i for i, num in enumerate(numbers) if num % 2 == 0]
print(even_indices)

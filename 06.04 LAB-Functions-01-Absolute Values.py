# Write a program that receives a sequence of numbers, separated by a single space, and prints
# their absolute value as a list. Use abs().

input_numbers = input("Enter numbers separated by a single space: ")
number_strings = input_numbers.split()
absolute_values = [abs(float(num)) for num in number_strings]
print(absolute_values)

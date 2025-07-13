# Write a program that receives a single string containing positive and negative numbers separated by
# a single space. Print a list containing the opposite of each number.

input_string = input()
number_strings = input_string.split()
opposites = []

for num in number_strings:
    number = int(num)
    opposites.append(-number)

print(opposites)
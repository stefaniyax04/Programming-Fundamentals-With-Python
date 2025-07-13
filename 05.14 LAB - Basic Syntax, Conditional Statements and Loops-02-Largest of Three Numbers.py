# Write a program that receives three whole numbers and prints the largest one.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

list_of_numbers = [number1, number2, number3]

largest_number = max(list_of_numbers)

print(largest_number)
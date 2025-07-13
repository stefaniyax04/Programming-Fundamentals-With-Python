# Write a program that reads four integer numbers. It should add the first to the second number, integer divide
# the sum by the third number, and multiply the result by the fourth number. Print the final result.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

sum = num1 + num2
divide = sum // num3
final = divide * num4

print(final)
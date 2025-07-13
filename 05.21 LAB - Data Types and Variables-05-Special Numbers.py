# Write a program that reads an integer n. Then, for all numbers in the range [1, n], print the number and
# if it is special or not (True / False). A number is special when the sum of its digits is 5, 7, or 11.

n = int(input("Enter a number: "))

for num in range(1, n + 1):
    digits_sum = sum(int(digit) for digit in str(num))
    is_special = digits_sum in [5, 7, 11]
    print(f"{num} -> {is_special}")

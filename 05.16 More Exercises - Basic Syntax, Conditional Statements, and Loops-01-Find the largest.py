# You will be given a number. Print the largest number that can be formed from the digits of the given number.

num = input()

sorted_digits = sorted(num, reverse=True)

largest = ""
for digit in sorted_digits:
    largest += digit

print(largest)

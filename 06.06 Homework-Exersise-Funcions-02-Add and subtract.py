# You will receive three integer numbers.
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.


def sum_numbers(a, b):
    return a + b


def subtract(sum_result, c):
    return sum_result - c


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    final_result = subtract(result, c)
    print(final_result)


a = int(input())
b = int(input())
c = int(input())

add_and_subtract(a, b, c)



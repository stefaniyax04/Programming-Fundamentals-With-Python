# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list
# of only the even numbers. Use filter().


def is_even(n):
    return n % 2 == 0


numbers = list(map(int, input().split()))
even_numbers = list(filter(is_even, numbers))

print(even_numbers)

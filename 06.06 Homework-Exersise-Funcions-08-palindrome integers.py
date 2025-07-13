# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function
# that receives a list of positive integers, separated by comma and space ", ". The function should check
# if each integer is a palindrome - True or False. Print the result.


def is_palindrome(numbers):
    return numbers == numbers[::-1]


def check_palindromes(numbers_str):
    numbers = numbers_str.split(", ")
    for num in numbers:
        print(is_palindrome(num))



numbers = input()
check_palindromes(numbers)
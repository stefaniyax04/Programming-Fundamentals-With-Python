# Using a list comprehension, write a program that receives numbers, separated by comma and space
# ", ", and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted as a positive number

numbers = list(map(int, input().split(", ")))

positives = [str(n) for n in numbers if n >= 0]
negatives = [str(n) for n in numbers if n < 0]
evens = [str(n) for n in numbers if n % 2 == 0]
odds = [str(n) for n in numbers if n % 2 != 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(evens)}")
print(f"Odd: {', '.join(odds)}")

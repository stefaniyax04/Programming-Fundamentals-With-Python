# Using comprehension, write a program that receives some text, separated by space, and
# takes only those words whose length is even. Print each word on a new line.

text = input().split()
[print(word) for word in text if len(word) % 2 == 0]

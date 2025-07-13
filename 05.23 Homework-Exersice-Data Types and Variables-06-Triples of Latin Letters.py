# Write a program that prints part of the ASCII table characters on the console,
# separated by a single space. On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print.

N = int(input())

for i in range(N):
    for j in range(N):
        for k in range(N):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")

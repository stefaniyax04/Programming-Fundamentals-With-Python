# Write a function that receives 3 characters. Concatenate all the characters
# into one string and print it on the console.

N = int(input())
P = int(input())

if N == P:
    print(1)
else:
    if N % P == 0:
        courses = N // P
    else:
        courses = (N // P) + 1
    print(courses)
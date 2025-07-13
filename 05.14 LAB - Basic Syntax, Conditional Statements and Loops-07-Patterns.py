# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.


n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print('*' * i)

for i in range(n - 1, 0, -1):
    print('*' * i)

# Write a function that receives three integer numbers and returns the smallest. Print the result on the console.
# Use an appropriate name for the function.


def find_smallest_of_three(a, b, c):
    return min(a, b, c)

a = int(input())
b = int(input())
c = int(input())

print(find_smallest_of_three(a, b, c))

# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print
# the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"


numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
min_num = min(sorted_numbers)
max_num = max(sorted_numbers)
sum_of_nums = sum(sorted_numbers)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_of_nums}")
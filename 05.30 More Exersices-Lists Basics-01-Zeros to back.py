# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements.
# Print the resulting integer list

n = int(input("Enter number of elements: "))

numbers = []
for i in range(n):
    number = int(input("Enter number: "))
    numbers.append(number)

result = []
zero_count = 0

for num in numbers:
    if num == 0:
        zero_count += 1
    else:
        result.append(num)

for i in range(zero_count):
    result.append(0)

print(result)

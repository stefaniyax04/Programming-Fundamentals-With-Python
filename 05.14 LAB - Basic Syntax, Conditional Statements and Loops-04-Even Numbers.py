# Write a program that receives a number n on the first line. On the following n lines, it receives different integer
# numbers. If the program receives an odd number, print "{num} is odd!" and end the program. Otherwise, if all numbers
# given are even, print "All numbers are even.".

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 != 0:
        print(f"{num} is odd!")
        break
else:
    print("All the number are even.")
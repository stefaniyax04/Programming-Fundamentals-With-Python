# You will receive two lines of input:
# · a list of employees' happiness as a string of numbers separated by a single space
# · a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# · If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# · Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

happiness = list(map(int, input().split()))
factor = int(input())

improved = [h * factor for h in happiness]
average = sum(improved) / len(improved)
happy_count = len([h for h in improved if h >= average])

if happy_count >= len(improved) / 2:
    print(f"Score: {happy_count}/{len(improved)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(improved)}. Employees are not happy!")


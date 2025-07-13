# Create a function that receives three parameters, calculates a result depending on the given operator, and returns
# it. Print the result of the function. The input comes as three parameters – an operator as a string and two integer
# numbers. The operator can be one of the following: "multiply", "divide", "add", and "subtract".

operator = str(input("Enter operator: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def solve(operator, num1, num2):
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = int(num1/num2)
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    return result


print(solve(operator, num1, num2))

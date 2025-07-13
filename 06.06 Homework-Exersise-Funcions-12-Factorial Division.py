# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.


def factorial_division(a, b):
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    fact_a = factorial(a)
    fact_b = factorial(b)
    result = fact_a / fact_b
    print(f"{result:.2f}")


a = int(input())
b = int(input())
factorial_division(a, b)

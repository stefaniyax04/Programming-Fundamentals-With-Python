# Write a program that rounds all the given numbers, separated
# by a single space, and prints the result as a list. Use round().

def round_numbers(numbers_str):
    numbers = numbers_str.split()
    result = []
    for num in numbers:
        result.append(round(float(num)))
    return result


input_numbers = input("Enter numbers: ")
rounded_list = round_numbers(input_numbers)
print(rounded_list)

# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
#
# 1 British Pound = 1.31 Dollars.

british_pound = int(input("Enter pounds: "))
us_dollars = british_pound * 1.31

print(f"{us_dollars:.3f}")
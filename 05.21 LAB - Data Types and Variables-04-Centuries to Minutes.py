# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minute.

centuries = int(input("Enter centuries: "))

year = centuries * 100
days = year * 365
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {year} years = {days} days = {hours} hours = {minutes} minutes")

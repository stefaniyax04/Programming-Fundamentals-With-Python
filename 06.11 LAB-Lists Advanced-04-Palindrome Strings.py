# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome. First, you should print a list containing
# all the found palindromes in the sequence. Then, you should print the number of occurrences
# of the given palindrome in the format: "Found palindrome {number} times"


words = input().split()
palindrome = input()

found = [word for word in words if word == word[::-1]]
count = found.count(palindrome)

print(found)
print(f"Found palindrome {count} times")

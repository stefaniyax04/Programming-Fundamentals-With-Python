# Using comprehension, write a program that receives a text and removes all its vowels,
# case insensitive. Print the new text string after removing the vowels. The vowels that
# should be considered are 'a', 'o', 'u', 'e', 'i'.

text = input("Enter text: ")
vowels = 'aeiouAEIOU'
no_vowels = ''.join([char for char in text if char not in vowels])
print("Text without vowels:", no_vowels)

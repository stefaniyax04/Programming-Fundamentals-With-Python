# Write a function that receives two characters and returns a single string with all the characters in
# between them (according to the ASCII code), separated by a single space. Print the result on the console.


def characters_in_range(char1, char2):
    start = ord(char1)
    end = ord(char2)
    if start > end:
        start, end = end, start

    result = ""
    for code in range(start + 1, end):
        result += chr(code) + " "
    return result.strip()


char1 = input()
char2 = input()

print(characters_in_range(char1, char2))

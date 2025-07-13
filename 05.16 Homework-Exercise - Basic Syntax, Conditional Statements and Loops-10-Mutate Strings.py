# You will be given two strings. Transform the first string into the second one, letter by letter,
# starting from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.


string1 = input()
string2 = input()

current_string_list = list(string1)
printed_strings = set()

for i in range(len(string1)):
    if current_string_list[i] != string2[i]:
        current_string_list[i] = string2[i]
        transformed_string = "".join(current_string_list)
        if transformed_string not in printed_strings:
            print(transformed_string)
            printed_strings.add(transformed_string)
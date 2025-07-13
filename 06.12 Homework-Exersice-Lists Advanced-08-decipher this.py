# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

words = input().split()
decoded_words = []
for word in words:
    number = ''
    i = 0
    while i < len(word) and word[i].isdigit():
        number += word[i]
        i += 1
    first_char = chr(int(number))
    rest = list(word[i:])
    if len(rest) > 1:
        rest[0], rest[-1] = rest[-1], rest[0]
    decoded_word = first_char + ''.join(rest)
    decoded_words.append(decoded_word)
print(' '.join(decoded_words))

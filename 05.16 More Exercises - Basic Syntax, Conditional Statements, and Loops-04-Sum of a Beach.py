# Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand",
# "Water", "Fish", and "Sun" appear (case insensitive)

text = input().lower()

keywords = ["sand", "water", "fish", "sun"]

count = 0
for word in keywords:
    count += text.count(word)

print(count)

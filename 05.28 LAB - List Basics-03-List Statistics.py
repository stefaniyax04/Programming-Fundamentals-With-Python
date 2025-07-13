# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# •	One with all the positive (including 0) numbers
# •	One with all the negative numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

n = int(input("Enter number of elements: "))
positive_list = []
negative_list = []

for i in range(n):
    number = int(input("Enter number: "))
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

count_of_positives = len(positive_list)
sum_of_negatives = sum(negative_list)

print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")

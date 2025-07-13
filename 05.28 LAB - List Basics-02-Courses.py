# On the first line, you will receive a single number n. On the following n lines, you will receive
# names of courses. You should create a list of courses and print it.

n = int(input("Enter number of elements: "))
courses = []

for i in range(n):
    current_course = input("Enter name of the course: ")
    courses.append(current_course)

print(courses)

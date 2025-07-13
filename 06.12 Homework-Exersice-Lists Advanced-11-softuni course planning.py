# Help plan the next Programming Fundamentals course by keeping track of the lessons that will be included in the
# course and all the exercises for the lessons. Before the course starts, there are some changes to be made.
# On the first input line, you will receive the initial schedule of lessons and exercises that will be part of the
# next course, separated by a comma and a space ", ". Until you receive the "course start" command, you will be given
# some commands to modify the course schedule.
# The possible commands are:
# •	"Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
# •	"Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
# •	"Remove:{lessonTitle}" - remove the lesson, if it exists.
# •	"Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# •	"Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson exists and
# there is no exercise already, in the following format "{lessonTitle}-Exercise". If the lesson doesn't exist, add the
# lesson at the end of the course schedule, followed by the Exercise.
# Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following
# the lessons.


schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add":
        lesson = parts[1]
        if lesson not in schedule:
            schedule.append(lesson)

    elif action == "Insert":
        lesson = parts[1]
        index = int(parts[2])
        if lesson not in schedule and 0 <= index <= len(schedule):
            schedule.insert(index, lesson)

    elif action == "Remove":
        lesson = parts[1]
        if lesson in schedule:
            schedule.remove(lesson)
        exercise = f"{lesson}-Exercise"
        if exercise in schedule:
            schedule.remove(exercise)

    elif action == "Swap":
        lesson1 = parts[1]
        lesson2 = parts[2]
        if lesson1 in schedule and lesson2 in schedule:
            index1 = schedule.index(lesson1)
            index2 = schedule.index(lesson2)
            schedule[index1], schedule[index2] = schedule[index2], schedule[index1]

            ex1 = f"{lesson1}-Exercise"
            ex2 = f"{lesson2}-Exercise"

            if ex1 in schedule:
                schedule.remove(ex1)
                schedule.insert(schedule.index(lesson1) + 1, ex1)
            if ex2 in schedule:
                schedule.remove(ex2)
                schedule.insert(schedule.index(lesson2) + 1, ex2)

    elif action == "Exercise":
        lesson = parts[1]
        exercise = f"{lesson}-Exercise"
        if lesson in schedule:
            if exercise not in schedule:
                idx = schedule.index(lesson)
                schedule.insert(idx + 1, exercise)
        else:
            schedule.append(lesson)
            schedule.append(exercise)

for i, lesson in enumerate(schedule, 1):
    print(f"{i}.{lesson}")



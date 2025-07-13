# You will receive a number representing the number of wagons a train has. Create a list (train) with the given
# length containing only zeros. Until you receive the command "End", you will receive some of the following commands
# · "add {people}" – you should add the number of people in the last wagon
# · "insert {index} {people}" - you should add the number of people at the given wagon
# · "leave {index} {people}" - you should remove the number of people from the wagon. There will
# be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.

n = int(input())
train = [0 for _ in range(n)]

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()
    action = parts[0]

    if action == "add":
        people = int(parts[1])
        train[-1] += people
    elif action == "insert":
        index = int(parts[1])
        people = int(parts[2])
        train[index] += people
    elif action == "leave":
        index = int(parts[1])
        people = int(parts[2])
        train[index] -= people

print(train)

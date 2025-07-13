def friends_report():
    friends = input().split(", ")

    blacklisted_count = 0
    lost_count = 0

    while True:
        command = input()

        if command == "Report":
            break

        parts = command.split()
        action = parts[0]

        if action == "Blacklist":
            name = parts[1]
            if name in friends:
                index = friends.index(name)
                friends[index] = "Blacklisted"
                blacklisted_count += 1
                print(f"{name} was blacklisted.")
            else:
                print(f"{name} was not found.")

        elif action == "Error":
            index = int(parts[1])
            if 0 <= index < len(friends):
                name = friends[index]
                if name != "Blacklisted" and name != "Lost":
                    friends[index] = "Lost"
                    lost_count += 1
                    print(f"{name} was lost due to an error.")

        elif action == "Change":
            index = int(parts[1])
            new_name = parts[2]
            if 0 <= index < len(friends):
                old_name = friends[index]
                friends[index] = new_name
                print(f"{old_name} changed his username to {new_name}.")

    print(f"Blacklisted names: {blacklisted_count}")
    print(f"Lost names: {lost_count}")
    print(" ".join(friends))


friends_report()
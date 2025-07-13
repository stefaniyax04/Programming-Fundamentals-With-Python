def chat_logger():
    chat = []

    while True:
        command = input()

        if command == "end":
            break

        parts = command.split()
        action = parts[0]

        if action == "Chat":
            message = " ".join(parts[1:])
            chat.append(message)

        elif action == "Delete":
            message = " ".join(parts[1:])
            if message in chat:
                chat.remove(message)

        elif action == "Edit":
            message = parts[1]
            edited = " ".join(parts[2:])
            if message in chat:
                index = chat.index(message)
                chat[index] = edited

        elif action == "Pin":
            message = " ".join(parts[1:])
            if message in chat:
                chat.remove(message)
                chat.append(message)

        elif action == "Spam":
            messages = parts[1:]
            chat.extend(messages)

    for message in chat:
        print(message)


chat_logger()

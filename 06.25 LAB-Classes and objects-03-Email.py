# Create class Email. The __init__ method should receive sender, receiver and a content.
# It should also have a default set to False attribute called is_sent. The class should have two additional methods:
# · send() - sets the is_sent attribute to True
# · get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by a single space) until you receive the command
# "Stop". The first element will be the sender, the second one – the receiver, and the third one –
# the content. On the final line, you will be given the indices of the sent emails separated by comma and space ", ".
# Call the send() method for the given indices of emails. For each email, call the get_info() method.


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    line = input()
    if line == "Stop":
        break
    parts = line.split()
    if len(parts) < 3:
        continue
    sender = parts[0]
    receiver = parts[1]
    content = " ".join(parts[2:])
    emails.append(Email(sender, receiver, content))

indices = [int(i) for i in input().split(", ")]

for index in indices:
    if 0 <= index < len(emails):
        emails[index].send()

for email in emails:
    print(email.get_info())




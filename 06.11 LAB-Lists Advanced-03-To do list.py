# You will be receiving to-do notes until you get the command "End". The notes will
# be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).

notes = []

while True:
    command = input()
    if command == "End":
        break
    importance, note = command.split("-", 1)
    notes.append((int(importance), note))

sorted_notes = [note for importance, note in sorted(notes)]
print(sorted_notes)

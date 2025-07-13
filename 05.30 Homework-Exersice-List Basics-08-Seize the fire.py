# The group of adventurists has gone on their first task. Now they should walk through fire - literally.
# They should use all the water they have left. Your task is to help them survive.
#
# Create a program that calculates the water needed to put out a "fire cell", based on the given
# information about its "fire level" and how much it gets affected by water.
#
# First, you will be given the level of fire inside the cell with the integer value of the cell,
# which represents the needed water to put out the fire. They will be given in the following format:
#
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
#
# Afterward, you will receive the amount of water you have for putting out the fires. There is a range
# of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not
# need to put it out.

cells_input = input()
water = int(input())

cells_data = cells_input.split("#")
valid_cells = []
effort = 0

for cell in cells_data:
    parts = cell.split(" = ")
    fire_type = parts[0]
    value = int(parts[1])

    is_valid = False
    if fire_type == "High" and 81 <= value <= 125:
        is_valid = True
    elif fire_type == "Medium" and 51 <= value <= 80:
        is_valid = True
    elif fire_type == "Low" and 1 <= value <= 50:
        is_valid = True

    if is_valid and water >= value:
        water -= value
        valid_cells.append(value)
        effort += value * 0.25

print("Cells:")
for cell in valid_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(valid_cells)}")

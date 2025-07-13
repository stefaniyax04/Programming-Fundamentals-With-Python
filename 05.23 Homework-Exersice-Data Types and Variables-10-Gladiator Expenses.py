# Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes
# the best snowballs. They have decided to involve you in their fray by writing a program that calculates
# snowball data and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Input
# •	On the first input line, you will receive N – the number of snowballs.
# •	On the next N*3 input lines, you will be receiving data about each snowball.
# Output
# •	You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
# Constraints
# •	The number of snowballs (N) will be an integer in the range [0, 100].
# •	The weight is an integer in the range [0, 1000].
# •	The time is an integer in the range [1, 500].
# •	The quality is an integer in the range [0, 100]

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = 0
sword_broken = 0
shield_broken = 0
armor_broken = 0

for fight in range(1, lost_fights + 1):
    helmet = fight % 2 == 0
    sword = fight % 3 == 0

    if helmet:
        helmet_broken += 1
    if sword:
        sword_broken += 1
    if helmet and sword:
        shield_broken += 1
        if shield_broken % 2 == 0:
            armor_broken += 1

expenses = (
    helmet_broken * helmet_price +
    sword_broken * sword_price +
    shield_broken * shield_price +
    armor_broken * armor_price
)

print(f"Gladiator expenses: {expenses:.2f} aureus")

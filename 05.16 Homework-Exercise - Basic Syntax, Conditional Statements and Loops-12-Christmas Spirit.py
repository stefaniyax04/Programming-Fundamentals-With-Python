# It is time to get in a Christmas mood. You need to decorate the house in time for the big event, but you have
# limited days to do so.
# Write a program that calculates how much money you will need to spend on Christmas decorations and how much your
# Christmas spirit will improve.
# On the first line, you will receive the quantity of decorations you should buy each time you go shopping.
# On the second line, you will receive the days left until Christmas.
# There are 4 types of decorations, and each piece costs a certain price. Also, each time you go shopping for
# a concrete type of decoration, your Christmas spirit is improved by some points:
# Until Christmas, you go shopping for a certain decoration as follows:
# •	Every second day, you buy Ornament Sets.
# •	Every third day, you buy Tree Skirts and Tree Garlands.
# •	Every fifth day, you buy Tree Lights.
# o	If you bought Tree Lights and Tree Garlands on the same day, you additionally increase your spirit by 30.
# Hint: Sometimes, the third and fifth days occur simultaneously (for example, the 15th day).
# That's not all! You have a cat at home that likes to mess around with the decorations:
# •	Every tenth day, your cat ruins all the tree decorations, and you lose 20 points of the spirit:
# o	Because of that, you go shopping (for a second time during the day) to buy one piece of a tree skirt,
# garlands, and lights, but you do NOT earn additional spirit points for them.
# •	Also, because of the cat, at the beginning of every eleventh day, you are forced to increase the quantity
# of decorations needed to be bought each time you go shopping by adding 2.
# •	When the last day is divisible by ten, the cat demolishes even more and ruins the Christmas turkey, then
# you lose an additional 30 points of spirit.
# Finally, you must print the total cost and the spirit gained.


quantity_per_shopping_trip = int(input())
days_until_christmas = int(input())

total_money_spent = 0
total_christmas_spirit = 0

DECORATIONS = {
    "Ornament Set": {"price": 2, "spirit": 5, "buy_day_modulo": 2},
    "Tree Skirt": {"price": 5, "spirit": 3, "buy_day_modulo": 3},
    "Tree Garland": {"price": 3, "spirit": 10, "buy_day_modulo": 3},
    "Tree Lights": {"price": 15, "spirit": 17, "buy_day_modulo": 5},
}

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_per_shopping_trip += 2

    if day % DECORATIONS["Ornament Set"]["buy_day_modulo"] == 0:
        total_money_spent += quantity_per_shopping_trip * DECORATIONS["Ornament Set"]["price"]
        total_christmas_spirit += DECORATIONS["Ornament Set"]["spirit"]

    if day % DECORATIONS["Tree Skirt"]["buy_day_modulo"] == 0:
        total_money_spent += quantity_per_shopping_trip * DECORATIONS["Tree Skirt"]["price"]
        total_christmas_spirit += DECORATIONS["Tree Skirt"]["spirit"]

        total_money_spent += quantity_per_shopping_trip * DECORATIONS["Tree Garland"]["price"]
        total_christmas_spirit += DECORATIONS["Tree Garland"]["spirit"]

    if day % DECORATIONS["Tree Lights"]["buy_day_modulo"] == 0:
        total_money_spent += quantity_per_shopping_trip * DECORATIONS["Tree Lights"]["price"]
        total_christmas_spirit += DECORATIONS["Tree Lights"]["spirit"]

        if day % DECORATIONS["Tree Garland"]["buy_day_modulo"] == 0:
            total_christmas_spirit += 30

    if day % 10 == 0:
        total_christmas_spirit -= 20
        total_money_spent += DECORATIONS["Tree Skirt"]["price"]
        total_money_spent += DECORATIONS["Tree Garland"]["price"]
        total_money_spent += DECORATIONS["Tree Lights"]["price"]

if days_until_christmas % 10 == 0:
    total_christmas_spirit -= 30

print(f"Total cost: {total_money_spent}")
print(f"Total spirit: {total_christmas_spirit}")
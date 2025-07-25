# Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
# Create a program that calculates how many loaves you can make (according to the recipe) with the budget you have.
# Here is the recipe for one loaf:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l
# First, you will receive your budget. Then, you will receive the price for 1 kg flour. The price for 1 pack
# of eggs is 75% of the price for 1 kg flour. The price for 1L milk is 25% more than the price for 1 kg flour.
# Keep in mind that you use only 250ml milk for a bread.
# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
# •	For every loaf of bread that you make, you will receive 3 colored eggs.
# •	For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs
# for your bread. The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves
# - ({current_bread_count} - 2)
# In the end, print the loaves of bread you made, the eggs you have collected, and the money you have left,
# formatted to the 2nd decimal place, in the following format:
# "You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."


def easter_bread():
    budget = float(input())
    price_flour = float(input())

    price_eggs = 0.75 * price_flour
    price_milk_per_l = 1.25 * price_flour
    price_milk_per_250ml = price_milk_per_l * 0.25

    cost_per_loaf = price_flour + price_eggs + price_milk_per_250ml

    loaves = 0
    colored_eggs = 0

    while budget >= cost_per_loaf:
        loaves += 1
        budget -= cost_per_loaf

        colored_eggs += 3

        if loaves % 3 == 0:
            eggs_lost = loaves - 2
            colored_eggs -= eggs_lost

    print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

easter_bread()

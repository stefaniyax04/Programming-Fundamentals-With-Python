# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money,
# so you decide to buy some items within your budget and then sell them at a higher price – with a 40% markup.
#
# You will receive a collection of items and a budget in the following format:
#
# {type->price|type->price|type->price……|type->price}
#
# {budget}
#
# The prices for each of the types cannot exceed a specific price, which is given below
# clothes - 50.00 , shoes - 35.00, accessories - 20.50
# If the price for a particular item is higher than the maximum price, don't buy it.
# Every time you buy an item, you have to reduce the budget with its price value. If you don't
# have enough money for it, you can't buy it. Buy as many items as you can.
#
# Next, you should increase the price of each item you have successfully bought by 40% and then
# sell it. Calculate if the budget after selling all the items is enough to buy the train ticket

items_input = input()
budget = float(input())

items = items_input.split("|")
bought_items = []
initial_spent = 0

for item in items:
    parts = item.split("->")
    item_type = parts[0]
    price = float(parts[1])

    valid = False
    if item_type == "Clothes" and price <= 50.00:
        valid = True
    elif item_type == "Shoes" and price <= 35.00:
        valid = True
    elif item_type == "Accessories" and price <= 20.50:
        valid = True

    if valid and budget >= price:
        budget -= price
        bought_items.append(price)
        initial_spent += price

resell_prices = []
total_resell = 0

for price in bought_items:
    new_price = price * 1.4
    resell_prices.append(new_price)
    total_resell += new_price

profit = total_resell - initial_spent
final_budget = budget + total_resell

formatted_prices = []
for price in resell_prices:
    formatted_prices.append(f"{price:.2f}")

print(" ".join(formatted_prices))
print(f"Profit: {profit:.2f}")

if final_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

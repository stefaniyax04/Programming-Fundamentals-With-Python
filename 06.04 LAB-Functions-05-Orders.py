# Write a function that calculates the total price of an order and returns it. The function should receive one of
# the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for
# a single piece of each product are:
# · coffee - 1.50
# · water - 1.00
# · coke - 1.40
# · snacks - 2.00
# Print the result formatted to the second decimal place.

def calculate_total(product, quantity):
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return price * quantity


product = input("Enter product: ")
quantity = int(input("Enter quantity of the product: "))
total = calculate_total(product, quantity)
print(f"{total:.2f}")


import math


def cooking_masterclass(budget, students, flour_price, egg_price, apron_price):
    aprons_needed = math.ceil(students * 1.2)
    eggs_needed = students * 10
    free_flour = students // 5
    flour_needed = students - free_flour

    total_cost = (
        aprons_needed * apron_price +
        eggs_needed * egg_price +
        flour_needed * flour_price
    )

    if total_cost <= budget:
        print(f"Items purchased for {total_cost:.2f}$.")
    else:
        needed = total_cost - budget
        print(f"{needed:.2f}$ more needed.")


budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

cooking_masterclass(budget, students, flour_price, egg_price, apron_price)

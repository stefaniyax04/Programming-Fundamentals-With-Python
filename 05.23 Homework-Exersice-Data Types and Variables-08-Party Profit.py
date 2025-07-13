# You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the
# number of lines, which will follow. On the following n lines, you will receive liters of water (integers),
# which you should pour into your tank. If the capacity is not enough, print "Insufficient capacity!" and continue
# reading the next line. On the last line, print the liters in the tank.

group_size = int(input())
days = int(input())

coins = 0
companions = group_size

for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    coins += 50
    coins -= 2 * companions
    if day % 3 == 0:
        coins -= 3 * companions
    if day % 5 == 0:
        coins += 20 * companions
        if day % 3 == 0:
            coins -= 2 * companions

coins_per_companion = coins // companions

print(f"{companions} companions received {coins_per_companion} coins each.")

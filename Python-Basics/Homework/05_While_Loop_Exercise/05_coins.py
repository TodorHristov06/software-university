change = float(input())

change_in_cents = round(change * 100)

coins = [200, 100, 50, 20, 10, 5, 2, 1]

coin_count = 0
index = 0  

while change_in_cents > 0:
    if change_in_cents >= coins[index]:
        change_in_cents -= coins[index]
        coin_count += 1
    else:
        index += 1  

print(coin_count)
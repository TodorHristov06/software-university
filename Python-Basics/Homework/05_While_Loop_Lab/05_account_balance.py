money = input()
total = 0;

while money != "NoMoreMoney":
    if float(money) < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {float(money):.2f}")
    total += float(money)
    money = input()
    
print(f"Total: {total:.2f}")
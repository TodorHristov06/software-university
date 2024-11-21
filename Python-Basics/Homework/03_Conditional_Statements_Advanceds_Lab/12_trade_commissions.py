city = input()
sales = float(input())

if city not in ["Sofia", "Plovdiv", "Varna"]:
    print("error")
elif sales < 0:
    print("error")
else:
    if city == "Sofia":
        if sales <= 500:
            commission = sales * 0.05
        elif sales <= 1000:
            commission = sales * 0.07
        elif sales <= 10000:
            commission = sales * 0.08
        else:
            commission = sales * 0.12
    elif city == "Plovdiv":
        if sales <= 500:
            commission = sales * 0.055
        elif sales <= 1000:
            commission = sales * 0.08
        elif sales <= 10000:
            commission = sales * 0.12
        else:
            commission = sales * 0.145
    elif city == "Varna":
        if sales <= 500:
            commission = sales * 0.045
        elif sales <= 1000:
            commission = sales * 0.075
        elif sales <= 10000:
            commission = sales * 0.10
        else:
            commission = sales * 0.13
    print(f"{commission:.2f}")
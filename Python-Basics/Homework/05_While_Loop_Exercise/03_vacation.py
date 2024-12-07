needed_money = float(input()) 
current_money = float(input())  

days_count = 0 
spend_days = 0  

while current_money < needed_money:
    action = input() 
    amount = float(input())  
    days_count += 1 

    if action == "spend":
        spend_days += 1  
        current_money -= amount  
        if current_money < 0:
            current_money = 0  
    elif action == "save":
        spend_days = 0  
        current_money += amount  

    if spend_days == 5:
        print("You can't save the money.")
        print(days_count)
        break
else:
    print(f"You saved the money for {days_count} days.")

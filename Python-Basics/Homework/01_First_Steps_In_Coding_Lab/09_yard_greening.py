square_meters = float(input())
price = square_meters * 7.61 
print(f"The final price is: {price - (price * 0.18):.2f} lv.")
print(f"The discount is: {price * 0.18:.2f} lv.")

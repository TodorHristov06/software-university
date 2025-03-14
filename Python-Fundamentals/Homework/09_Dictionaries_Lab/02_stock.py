elements = input().split(" ")
searched_products = input().split(" ")
stock = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    stock[key] = int(value)

for product in searched_products:
    if product in stock:
        print (f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

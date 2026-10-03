your_cart = {}

while True:
    item = input("Enter an item to add to your cart (or type 'check out' if finished): ")
    if item == 'check out':
        break
    price_tag = float(input(f"Enter the price of {item}: "))
    your_cart[item] = (price_tag)

print(your_cart)

total_price = 0
for price in your_cart.values():
    total_price = total_price + price
print(f"Total price: {total_price:.2f}")

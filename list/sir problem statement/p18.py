cart = ["apple","mango","banana"]

item = input("Enter item: ")
cart.append(item)

item = input("Enter another item: ")
cart.append(item)

item = input("Enter item to remove: ")
if item in cart:
    cart.remove(item)

item = input("Enter item to search: ")
if item in cart:
    print("Item found")
else:
    print("Item not found")

print("Cart:", cart)
print("Total items:", len(cart))

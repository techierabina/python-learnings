def add_item(cart):
    name=input("Item name: ")
    if name.lower()=='done':
        return False
    price=float(input("Price per unit: "))
    quantity=int(input("Quantity: "))
    item={"name":name,"price":price,"quantity":quantity}
    cart.append(item)
    print(f"✅ Added {quantity} x {name} at ${price:.2f} each.")
    return True

def show_cart(cart):
    print("\n🛒 Your Cart:")
    for item in cart:
        item_total=item["price"]*item["quantity"]
        print(f"- {item['name']} (x{item['quantity']}): ${item_total:.2f}")

def calculate_total(cart):
    total=0
    for item in cart:
        total+=item["price"]*item["quantity"]
    return total

cart=[]
print("Welcome to Shopping Cart!")
while True:
    print("\nAdd item to cart (or type 'done' as item name to finish):")
    if not add_item(cart):
        break

show_cart(cart)
total_cost = calculate_total(cart)
print(f"\n💰 Total Cost: ${total_cost:.2f}")
print("Thank you for shopping!")
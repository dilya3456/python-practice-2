customer = input("Enter customer name: ")

subtotal = 0.0
items_count = 0

while True:
    item_name = input("Enter item name (or 'done' to finish): ")

    if item_name.lower() == "done":
        break

    price = float(input("Enter price: "))
    subtotal += price
    items_count += 1

print("Customer :", customer.upper())
print("Items :", items_count)
print("Subtotal :", subtotal, "KZT")

hour = int(input("Enter current hour (0-23): "))
print("-" * 30)

if 6 <= hour < 12:
    discount_label = "Morning discount"
    discount = subtotal * 0.10
    discounted_subtotal = subtotal - discount
    tip = discounted_subtotal * 0.10
    total = discounted_subtotal + tip

    print("Time period :", discount_label)
    print("Discount :", discount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", total, "KZT")

elif 12 <= hour < 17:
    discount_label = "No discount"
    discount = 0.0
    discounted_subtotal = subtotal - discount
    tip = discounted_subtotal * 0.10
    total = discounted_subtotal + tip

    print("Time period :", discount_label)
    print("Discount :", discount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", total, "KZT")

elif 17 <= hour < 22:
    discount_label = "Evening discount"
    discount = subtotal * 0.05
    discounted_subtotal = subtotal - discount
    tip = discounted_subtotal * 0.10
    total = discounted_subtotal + tip

    print("Time period :", discount_label)
    print("Discount :", discount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", total, "KZT")

else:
    print("Closed")

print("-" * 30)

print("Name uppercase :", customer.upper())
print("Name lowercase :", customer.lower())
print("Name length :", len(customer))

if customer[0].upper() == "A" or customer[0].upper() == "S":
    print("VIP customer")
else:
    print("Regular customer")

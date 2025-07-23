# Simple Pizza Order Program

print("Welcome to Pizza Place!")

# Get user input
size = input("Choose a size (S/M/L): ")
topping = input("Choose a topping (Pepperoni/Mushrooms/Cheese): ")
extra_cheese = input("Do you want extra cheese? (yes/no): ")

# Price calculation
price = 0

if size.upper() == "S":
    price += 8
elif size.upper() == "M":
    price += 10
elif size.upper() == "L":
    price += 12
else:
    print("Invalid size selected.")

if topping.lower() == "pepperoni":
    price += 2
elif topping.lower() == "mushrooms":
    price += 1.5
elif topping.lower() == "cheese":
    price += 1

if extra_cheese.lower() == "yes":
    price += 1

# Final summary
print("\n--- Order Summary ---")
print(f"Size: {size.upper()}")
print(f"Topping: {topping}")
print(f"Extra Cheese: {extra_cheese.capitalize()}")
print(f"Total Price: ${price:.2f}")

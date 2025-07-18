def order_pizza():
    menu = {
        1: ("Margherita", 250),
        2: ("Pepperoni", 300),
        3: ("Veggie", 270),
        4: ("BBQ Chicken", 320)
    }

    print("Welcome to Python Pizza!")
    print("Menu:")
    for key, (name, price) in menu.items():
        print(f"{key}. {name} - ₹{price}")

    choice = int(input("Enter the number of the pizza you want to order: "))

    if choice in menu:
        pizza, price = menu[choice]
        print(f"\nYou have ordered a {pizza}.")
        print(f"Please pay ₹{price}. Thank you!")
    else:
        print("Invalid choice. Please try again.")

order_pizza()

cart = {}

while True:
    print("\n----- Shopping Cart Menu -----")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart[item] = price
        print("Item added successfully!")

    elif choice == "2":
        item = input("Enter item name to remove: ")

        if item in cart:
            del cart[item]
            print("Item removed successfully!")
        else:
            print("Item not found!")

    elif choice == "3":
        print("\nItems in Cart:")

        if len(cart) == 0:
            print("Cart is empty")
        else:
            for item, price in cart.items():
                print(item, ":", price)

    elif choice == "4":
        total = sum(cart.values())
        print("Total Amount =", total)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
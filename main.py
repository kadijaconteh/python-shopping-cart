products = {"A Bag of Rice": 1500.00, "Bread": 12.00, "Milk": 50.00, "A Bag of Sugar": 1000.00}
cart = []
running = True

while running:
    print("\n****Welcome to Dija's Store****")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove Item from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter an option between (1-6): ")
    
    # View Products
    if choice == "1":
        print("Available Products: ") 
        for item, price in products.items():
            print(f"{item} - D{price:.2f}")
    # Add to Cart
    elif choice == "2":
        print("Which Product/Products would you like to add to your Cart?")
        cart_input = input("Enter Product option (rice/bread/milk/sugar/all): ").lower()
        # Mapping input to product names
        if cart_input == "rice":
            cart.append("A Bag of Rice")
            print("A Bag of Rice - D1500.00 added to cart!")
        elif cart_input == "bread":
            cart.append("Bread")
            print("Bread - D12.00 added to cart!")
        elif cart_input == "milk":
            cart.append("Milk")
            print("Milk - D50.00 added to cart!")
        elif cart_input == "sugar":
            cart.append("A Bag of Sugar")
            print("A Bag of Sugar - D1000.00 added to cart!")
        elif cart_input == "all":
            cart = list(products.keys())
            print("All products added to cart!")
        else:
            print("Invalid Input.")
    # View Cart
    elif choice == "3":
        if cart:
            print("Your Cart: ")
            total = 0
            for item in cart:
                print(f"{item} - D{products[item]:.2f}")
                total += products[item]
                print(f"Total: D{total:.2f}")
        else:
            print("Your cart is empty.")
    # Remove Item from Cart
    elif choice == "4":
        if cart:
            item_to_remove = input("Enter product name to remove: ").lower()
            mapping = {"rice": "A Bag of Rice", "bread": "Bread", "milk": "Milk", "sugar": "A Bag of Sugar"}
            if item_to_remove in mapping and mapping[item_to_remove] in cart:
                cart.remove(mapping[item_to_remove])
                print(f"{mapping[item_to_remove]} removed from cart.")
            else:
                print("That item is not in your cart.")
        else:
            print("Your cart is empty.")
    # Checkout
    elif choice == "5":
        if cart:
            total = sum(products[item] for item in cart)    
            print(f"Checkout complete! Your total is D{total:.2f}") 
            cart = []
        else:
            print("Your cart is empty")
    #Exit
    elif choice == "6":
        print("You have chosen to exit this program. \nThank you for stopping by!")
        running = False
    #Invalid menu input
    else:
        print("Invalid option. Please choose 1-6.")

        

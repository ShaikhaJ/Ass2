from EBookStore import EBook, AudioBook, Customer, ShoppingCart, Order, Invoice, Payment

# --- Simulate The Great E-books Store ---
def the_great_ebooks_store():
    print("Welcome to The Great E-books Store!\n")
    print("We offer a wide selection of E-Books and AudioBooks.\n")

    # --- Initialize Books ---
    book_list = [
        EBook("Book1", "Author1", "2021-06-12", "Genre1", 15.99),
        EBook("Book2", "Author2", "2019-04-25", "Genre2", 22.49),
        EBook("Book3", "Author3", "2018-11-30", "Genre3", 8.99),
        EBook("Book4", "Author4", "2020-08-15", "Genre4", 12.75),
        EBook("Book5", "Author5", "2022-01-20", "Genre5", 18.95),
        AudioBook("Book6", "Author6", "2021-09-10", "Genre6", 25.00, 120, "Narrator1", "MP3",
                  300),
        AudioBook("Book7", "Author7", "2019-03-01", "Genre7", 14.99, 90, "Narrator2", "MP3",
                  250)
    ]

    # Display all available books
    print("Here are some of our available books and audiobooks:\n")
    for idx, book in enumerate(book_list, 1):
        print(f"{idx}. {book}")
    print("\n")

    # --- Initialize Customers ---
    customer1 = Customer("Alice", "123-456-7890", "alice@example.com", loyalty_status=True)
    customer2 = Customer("Bob", "234-567-8901", "bob@example.com")
    customer3 = Customer("Carol", "345-678-9012", "carol@example.com")


    # --- Customer 1 (Loyal Member) ---
    print("Customer 1: Alice (Loyal Member) shopping!\n")
    print(customer1)
    order1 = Order("ORD001", customer1)

    # Alice adds books to cart
    order1.add_to_order(book_list[0])
    order1.add_to_order(book_list[1])
    print(f"Alice's cart: {order1}\n")

    # Alice removes a book from cart
    order1.remove_from_order(book_list[1])
    print(f"Alice's cart after removal: {order1}\n")

    # Applying discount for Alice
    final_total1, discount1, vat1 = order1.apply_discount()
    print(f"Alice's order summary (with discount):")
    print(f"Discount Applied: {discount1}% | VAT: ${vat1:.2f} | Final Total: ${final_total1:.2f}\n")

    # Generate and show Invoice for Alice
    invoice1 = Invoice("ORD001", final_total1, discount1, vat1)
    print("Invoice for Alice:")
    print(invoice1)
    print("\n")

    # Process Payment for Alice
    payment1 = Payment("ORD001", final_total1, "Credit Card")
    print("Payment processed for Alice:")
    print(payment1)
    print("\n")

    # --- Customer 2: Bob ---
    print("Customer 2: Bob (Non-Loyal Member) shopping!\n")
    print(customer2)
    order2 = Order("ORD002", customer2)
    order2.add_to_order(book_list[2])
    order2.add_to_order(book_list[3])
    print(f"Bob's cart: {order2}\n")

    # Applying discount for Bob
    final_total2, discount2, vat2 = order2.apply_discount()
    print(f"Bob's order summary (with discount):")
    print(f"Discount Applied: {discount2}% | VAT: ${vat2:.2f} | Final Total: ${final_total2:.2f}\n")

    # Generate and show Invoice for Bob
    invoice2 = Invoice("ORD002", final_total2, discount2, vat2)
    print("Invoice for Bob:")
    print(invoice2)
    print("\n")

    # Process Payment for Bob
    payment2 = Payment("ORD002", final_total2, "PayPal")
    print("Payment processed for Bob:")
    print(payment2)
    print("\n")

    # --- Customer 3: Carol ---
    print("Customer 3: Carol (Non-Loyal Member) shopping!\n")
    print(customer3)
    order3 = Order("ORD003", customer3)
    order3.add_to_order(book_list[4])
    print(f"Carol's cart: {order3}\n")

    # Applying discount for Carol
    final_total3, discount3, vat3 = order3.apply_discount()
    print(f"Carol's order summary (with discount):")
    print(f"Discount Applied: {discount3}% | VAT: ${vat3:.2f} | Final Total: ${final_total3:.2f}\n")

    # Generate and show Invoice for Carol
    invoice3 = Invoice("ORD003", final_total3, discount3, vat3)
    print("Invoice for Carol:")
    print(invoice3)
    print("\n")

    # Process Payment for Carol
    payment3 = Payment("ORD003", final_total3, "Debit Card")
    print("Payment processed for Carol:")
    print(payment3)
    print("\n")

    # Final Thank You Message
    print("Thank you for shopping at The Great E-books Store! We hope to see you again.\n")


# Run the simulation
the_great_ebooks_store()


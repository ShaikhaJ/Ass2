from EBookStore import EBook, AudioBook, Customer, ShoppingCart, Order, Invoice, Payment  # Importing classes from the EBookStore py

def the_great_ebooks_store():
    print("=" * 40)  # Print a line for decoration
    print("  Welcome to The Great E-books Store!")  # Welcome message
    print("=" * 40)  # Print a line for decoration
    print("We offer a wide selection of EBooks and AudioBooks.\n")  # Explanation about the store

    # List of available books (both EBooks and AudioBooks)
    book_list = [
        EBook("Book1", "Author1", "2021-06-12", "Genre1", 15.99),
        EBook("Book2", "Author2", "2019-04-25", "Genre2", 22.49),
        EBook("Book3", "Author3", "2018-11-30", "Genre3", 8.99),
        EBook("Book4", "Author4", "2020-08-15", "Genre4", 12.75),
        EBook("Book5", "Author5", "2022-01-20", "Genre5", 18.95),
        AudioBook("AudioBook1", "Author6", "2021-09-10", "Genre6", 25.00, 120, "Narrator1", "MP3",
                  300),
        AudioBook("AudioBook2", "Author7", "2019-03-01", "Genre7", 14.99, 90, "Narrator2", "MP3",
                  250)
    ]

    # Display all available books
    print("-" * 40)  # Print a separator line
    print("Available Books and Audiobooks:")  # Display header
    print("-" * 40)  # Print a separator line
    for idx, book in enumerate(book_list, 1):  # Loop through the books and audiobooks
        print(f"{idx}. {book} \n")  # Print each book's details
    print("\n")  # Print a newline for spacing

    # Creating customer instances
    customer1 = Customer("Alice", "123-456-7890", "alice@example.com", loyalty_status=True)  # Loyal customer
    customer2 = Customer("Bob", "234-567-8901", "bob@example.com")  # Non-loyal customer
    customer3 = Customer("Carol", "345-678-9012", "carol@example.com")  # Non-loyal customer buying in bulk

    print("=" * 40)  # Print a separator line
    print("Customer 1: Alice (Loyal Member) shopping!")  # Display that Alice is shopping
    print("=" * 40)  # Print a separator line
    print(customer1)  # Display Alice's details
    order1 = Order("ORD001", customer1)  # Create an order for Alice

    # Alice adds books to cart
    print("\n-- Adding Books to Alice's Cart --")  # Header for adding books
    order1.add_to_order(book_list[0])  # Add the first book to Alice's cart
    order1.add_to_order(book_list[1])  # Add the second book to Alice's cart
    print(f"\nAlice's cart summary:\n{order1}\n")  # Print Alice's cart summary

    # Alice removes a book from cart
    print("\n-- Removing a Book from Alice's Cart --")  # Header for removing books
    order1.remove_from_order(book_list[1])  # Remove the second book from Alice's cart
    print(f"\nAlice's cart after removal:\n{order1}\n")  # Print updated cart summary after removal

    # Applying discount for Alice
    print("-- Applying Discount for Alice --")  # Header for discount application
    final_total1, discount1, vat1 = order1.apply_discount()  # Apply discount and calculate totals
    print(
        f"\nOrder Summary for Alice:\nDiscount: {discount1}% | VAT: ${vat1:.2f} | Final Total: ${final_total1:.2f}\n")  # Print order summary for Alice

    # Generate and show Invoice for Alice
    print("-" * 40)  # Print a separator line
    print("Invoice for Alice")  # Header for invoice
    print("-" * 40)  # Print a separator line
    invoice1 = Invoice("ORD001", final_total1, discount1, vat1)  # Create an invoice for Alice
    print(invoice1, "\n")  # Print the invoice

    # Process Payment for Alice
    print("-" * 40)  # Print a separator line
    print("Payment processed for Alice")  # Header for payment processing
    print("-" * 40)  # Print a separator line
    payment1 = Payment("ORD001", final_total1, "Credit Card")  # Create a payment for Alice
    print(payment1, "\n")  # Print the payment details

    # Customer 2: Bob (Non-loyal)
    print("=" * 40)  # Print a separator line
    print("Customer 2: Bob (Non-Loyal Member) shopping!")  # Display that Bob is shopping
    print("=" * 40)  # Print a separator line
    print(customer2)  # Print Bob's details
    order2 = Order("ORD002", customer2)  # Create an order for Bob

    # Bob adds books to cart
    print("\n-- Adding Books to Bob's Cart --")  # Header for adding books
    order2.add_to_order(book_list[2])  # Add the third book to Bob's cart
    order2.add_to_order(book_list[3])  # Add the fourth book to Bob's cart
    print(f"\nBob's cart summary:\n{order2}\n")  # Print Bob's cart summary

    # Applying discount for Bob
    print("-- Applying Discount for Bob --")  # Header for discount application
    final_total2, discount2, vat2 = order2.apply_discount()  # Apply discount and calculate totals
    print(
        f"\nOrder Summary for Bob:\nDiscount: {discount2}% | VAT: ${vat2:.2f} | Final Total: ${final_total2:.2f}\n")  # Print order summary for Bob

    # Generate and show Invoice for Bob
    print("-" * 40)  # Print a separator line
    print("Invoice for Bob")  # Header for invoice
    print("-" * 40)  # Print a separator line
    invoice2 = Invoice("ORD002", final_total2, discount2, vat2)  # Create an invoice for Bob
    print(invoice2, "\n")  # Print the invoice

    # Process Payment for Bob
    print("-" * 40)  # Print a separator line
    print("Payment processed for Bob")  # Header for payment processing
    print("-" * 40)  # Print a separator line
    payment2 = Payment("ORD002", final_total2, "PayPal")  # Create a payment for Bob
    print(payment2, "\n")  # Print the payment details

    # Customer 3: Carol (Non-loyal)
    print("=" * 40)  # Print a separator line
    print("Customer 3: Carol (Non-Loyal Member) shopping!")  # Display that Carol is shopping
    print("=" * 40)  # Print a separator line
    print(customer3)  # Print Carol's details
    order3 = Order("ORD003", customer3)  # Create an order for Carol

    # Carol adds books to cart
    print("\n-- Adding Books to Carol's Cart --")  # Header for adding books
    order3.add_to_order(book_list[1])  # Add the second book to Carol's cart
    order3.add_to_order(book_list[2])  # Add the third book to Carol's cart
    order3.add_to_order(book_list[3])  # Add the fourth book to Carol's cart
    order3.add_to_order(book_list[4])  # Add the fifth book to Carol's cart
    order3.add_to_order(book_list[5])  # Add the first audiobook to Carol's cart
    order3.add_to_order(book_list[6])  # Add the second audiobook to Carol's cart
    print(f"\nCarol's cart summary:\n{order3}\n")  # Print Carol's cart summary

    # Carol removes a book from cart
    print("\n-- Removing a Book from Carol's Cart --")  # Header for removal
    order3.remove_from_order(book_list[2])  # Remove the third book from Carol's cart
    print(f"\nCarol's cart after removal:\n{order3}\n")  # Print updated cart after removal

    # Applying discount for Carol
    print("-- Applying Discount for Carol --")  # Header for discount application
    final_total3, discount3, vat3 = order3.apply_discount()  # Apply discount and calculate totals
    print(
        f"\nOrder Summary for Carol:\nDiscount: {discount3}% | VAT: ${vat3:.2f} | Final Total: ${final_total3:.2f}\n")  # Print order summary for Carol

    # Generate and show Invoice for Carol
    print("-" * 40)  # Print a separator line
    print("Invoice for Carol")  # Header for invoice
    print("-" * 40)  # Print a separator line
    invoice3 = Invoice("ORD003", final_total3, discount3, vat3)  # Create an invoice for Carol
    print(invoice3, "\n")  # Print the invoice

    # Process Payment for Carol
    print("-" * 40)  # Print a separator line
    print("Payment processed for Carol")  # Header for payment processing
    print("-" * 40)  # Print a separator line
    payment3 = Payment("ORD003", final_total3, "Debit Card")  # Create a payment for Carol
    print(payment3, "\n")  # Print the payment details

    # End message
    print("=" * 40)  # Print a separator line
    print("Thank you for shopping at The Great E-books Store! We hope to see you again.")  # Thank you message
    print("=" * 40)  # Print a separator line


# Run the simulation
the_great_ebooks_store()




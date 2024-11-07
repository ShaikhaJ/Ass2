from datetime import date

class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title  # Title of the ebook (private)
        self.__author = author  # Author of the ebook (private)
        self.__publication_date = publication_date  # Publication date of the ebook (private)
        self.__genre = genre  # Genre of the ebook (private)
        self.__price = price  # Price of the ebook (private)

    def get_title(self):
        return self.__title  # Return the title of the ebook

    def get_price(self):
        return self.__price  # Return the price of the ebook

    def __str__(self):
        # Return a formatted string with ebook details
        return (f"EBook:\nTitle: {self.__title}\nAuthor: {self.__author}\n"
                f"Genre: {self.__genre}\nPublished: {self.__publication_date}\n"
                f"Price: ${self.__price:.2f}")

class AudioBook(EBook): #Inherited from EBook
    def __init__(self, title, author, publication_date, genre, price, duration, narrator, audio_format, file_size):
        super().__init__(title, author, publication_date, genre, price)  # Call the parent (EBook) constructor
        self._duration = duration  # Duration of the audiobook (protected)
        self._narrator = narrator  # Narrator of the audiobook (protected)
        self._audio_format = audio_format  # Audio format of the audiobook (protected)
        self._file_size = file_size  # File size of the audiobook (protected)

    def __str__(self):
        # Return a formatted string with audiobook details, including parent class details
        return (f"AudioBook:\n{super().__str__()}\nDuration: {self._duration} min\n"
                f"Narrator: {self._narrator}\nFormat: {self._audio_format}\nSize: {self._file_size}MB")

class Customer:
    def __init__(self, name, contact_info, email, loyalty_status=False):
        self.__name = name  # Customer's name (private)
        self.__contact_info = contact_info  # Customer's contact info (private)
        self.__email = email  # Customer's email (private)
        self.__loyalty_status = loyalty_status  # Customer's loyalty status (private)

    def get_name(self):
        return self.__name  # Return the customer's name

    def get_loyalty_status(self):
        return self.__loyalty_status  # Return the loyalty status of the customer

    def __str__(self):
        # Return a formatted string with customer details
        status = "Loyal Member" if self.__loyalty_status else "Non-Loyal Member"
        return (f"Customer:\nName: {self.__name}\nContact: {self.__contact_info}\n"
                f"Email: {self.__email}\nStatus: {status}")

class ShoppingCart: #Composition with EBook
    def __init__(self):
        self.__cart_items = []  # List of cart items (ebooks) (private)
        self.__total_price = 0.0  # Total price of the cart (private)
        self.__quantity = 0  # Quantity of items in the cart (private)
        self.__created_date = date.today()  # Creation date of the cart (private)

    def add_item(self, ebook):
        self.__cart_items.append(ebook)  # Add an ebook to the cart
        self.__total_price += ebook.get_price()  # Add ebook's price to total price
        self.__quantity += 1  # Increment quantity
        print(f"Added '{ebook.get_title()}' to cart.")  # Print confirmation

    def remove_item(self, ebook):
        if ebook in self.__cart_items:
            self.__cart_items.remove(ebook)  # Remove ebook from the cart
            self.__total_price -= ebook.get_price()  # Subtract ebook's price from total
            self.__quantity -= 1  # Decrease quantity
            print(f"Removed '{ebook.get_title()}' from cart.")  # Print confirmation

    def calculate_total(self):
        return self.__total_price  # Return the total price of the cart

    def get_items(self):
        return self.__cart_items  # Return the list of items (ebooks) in the cart

    def __str__(self):
        # Return a formatted string with cart details
        items = '\n  '.join([f"- {item.get_title()}" for item in self.__cart_items])  # List of items
        return (f"Shopping Cart:\nDate Created: {self.__created_date}\nItems:\n  {items}\n"
                f"Total Quantity: {self.__quantity}\nTotal Price: ${self.__total_price:.2f}")

class Order: #Association with Customer, Aggregation with ShoppingCart
    def __init__(self, order_id, customer):
        self.__order_id = order_id  # Order ID (private)
        self.__customer = customer  # Customer placing the order (private)
        self.__order_date = date.today()  # Order date (private)
        self.__cart = ShoppingCart()  # ShoppingCart associated with the order (aggregation)
        self.__discount = 0.0  # Discount for the order (private)

    def add_to_order(self, ebook):
        self.__cart.add_item(ebook)  # Add ebook to the order's cart

    def remove_from_order(self, ebook):
        self.__cart.remove_item(ebook)  # Remove ebook from the order's cart

    def apply_discount(self):
        total = self.__cart.calculate_total()  # Get the total price from the cart
        if self.__customer.get_loyalty_status():
            self.__discount = 0.10  # 10% discount for loyal customers
        elif len(self.__cart.get_items()) >= 5:
            self.__discount = 0.20  # 20% discount for bulk orders
        discounted_total = total * (1 - self.__discount)  # Apply discount to total price
        vat = discounted_total * 0.08  # 8% VAT
        final_total = discounted_total + vat  # Final total including VAT
        return final_total, self.__discount * 100, vat  # Return final total, discount, and VAT

    def __str__(self):
        # Return a formatted string with order details
        cart_info = str(self.__cart)  # Get the cart summary
        return (f"Order:\nOrder ID: {self.__order_id}\nOrder Date: {self.__order_date}\n"
                f"Customer: {self.__customer.get_name()}\n{cart_info}")

class Invoice: #Association with Order
    def __init__(self, order_id, amount, discount, vat):
        self.__invoice_id = f"INV-{order_id}"  # Invoice ID based on order ID (private)
        self.__amount = amount  # Total amount to pay (private)
        self.__discount = discount  # Discount applied (private)
        self.__vat = vat  # VAT amount (private)
        self.__issue_date = date.today()  # Issue date of the invoice (private)

    def __str__(self):
        # Return a formatted string with invoice details
        return (f"Invoice:\nInvoice ID: {self.__invoice_id}\nIssue Date: {self.__issue_date}\n"
                f"Amount: ${self.__amount:.2f}\nDiscount: {self.__discount:.0f}%\nVAT: ${self.__vat:.2f}")

class Payment: #Association with Invoice
    def __init__(self, invoice_id, amount, method):
        self.__payment_id = f"PAY-{invoice_id}"  # Payment ID based on invoice ID (private)
        self.__amount = amount  # Payment amount (private)
        self.__method = method  # Payment method (private)
        self.__payment_date = date.today()  # Payment date (private)

    def __str__(self):
        # Return a formatted string with payment details
        return (f"Payment:\nPayment ID: {self.__payment_id}\nDate: {self.__payment_date}\n"
                f"Amount: ${self.__amount:.2f}\nMethod: {self.__method}")

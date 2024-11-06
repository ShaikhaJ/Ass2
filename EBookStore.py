from datetime import date

class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f"EBook: {self.__title} by {self.__author} | Genre: {self.__genre} | "
                f"Published: {self.__publication_date} | Price: ${self.__price:.2f}")


class AudioBook(EBook):
    def __init__(self, title, author, publication_date, genre, price, duration, narrator, audio_format, file_size):
        super().__init__(title, author, publication_date, genre, price)
        self.__duration = duration
        self.__narrator = narrator
        self.__audio_format = audio_format
        self.__file_size = file_size

    def __str__(self):
        return (f"AudioBook: {super().__str__()} | Duration: {self.__duration} min | "
                f"Narrator: {self.__narrator} | Format: {self.__audio_format} | Size: {self.__file_size}MB")


class Customer:
    def __init__(self, name, contact_info, email, loyalty_status=False):
        self.__name = name
        self.__contact_info = contact_info
        self.__email = email
        self.__loyalty_status = loyalty_status

    def get_name(self):
        return self.__name

    def get_loyalty_status(self):
        return self.__loyalty_status

    def __str__(self):
        status = "Loyal Member" if self.__loyalty_status else "Non-Loyal Member"
        return (f"Customer: {self.__name} | Contact: {self.__contact_info} | "
                f"Email: {self.__email} | Status: {status}")


class ShoppingCart:
    def __init__(self):
        self.__cart_items = []
        self.__total_price = 0.0
        self.__quantity = 0
        self.__created_date = date.today()

    def add_item(self, ebook):
        self.__cart_items.append(ebook)
        self.__total_price += ebook.get_price()
        self.__quantity += 1
        print(f"Added '{ebook.get_title()}' to cart.")

    def remove_item(self, ebook):
        if ebook in self.__cart_items:
            self.__cart_items.remove(ebook)
            self.__total_price -= ebook.get_price()
            self.__quantity -= 1
            print(f"Removed '{ebook.get_title()}' from cart.")

    def calculate_total(self):
        return self.__total_price

    def get_items(self):
        return self.__cart_items

    def __str__(self):
        items = ', '.join([item.get_title() for item in self.__cart_items])
        return (f"Cart Created: {self.__created_date} | Cart Items: [{items}] | "
                f"Quantity: {self.__quantity} | Total Price: ${self.__total_price:.2f}")


class Order:
    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = date.today()
        self.__cart = ShoppingCart()
        self.__discount = 0.0

    def add_to_order(self, ebook):
        self.__cart.add_item(ebook)

    def remove_from_order(self, ebook):
        self.__cart.remove_item(ebook)

    def apply_discount(self):
        total = self.__cart.calculate_total()
        if self.__customer.get_loyalty_status():
            self.__discount = 0.10  # 10% discount for loyal customers
        elif len(self.__cart.get_items()) >= 5:
            self.__discount = 0.20  # 20% discount for bulk orders
        discounted_total = total * (1 - self.__discount)
        vat = discounted_total * 0.08  # 8% VAT
        final_total = discounted_total + vat
        return final_total, self.__discount * 100, vat

    def __str__(self):
        cart_info = str(self.__cart)
        return (f"Order ID: {self.__order_id} | Order Date: {self.__order_date} | "
                f"Customer: {self.__customer.get_name()} | Cart Info: {cart_info}")


class Invoice:
    def __init__(self, order_id, amount, discount, vat):
        self.__invoice_id = f"INV-{order_id}"
        self.__amount = amount
        self.__discount = discount
        self.__vat = vat
        self.__issue_date = date.today()

    def __str__(self):
        return (f"Invoice ID: {self.__invoice_id} | Issue Date: {self.__issue_date} | "
                f"Amount: ${self.__amount:.2f} | Discount: {self.__discount:.0f}% | VAT: ${self.__vat:.2f}")


class Payment:
    def __init__(self, invoice_id, amount, method):
        self.__payment_id = f"PAY-{invoice_id}"
        self.__amount = amount
        self.__method = method
        self.__payment_date = date.today()

    def __str__(self):
        return (f"Payment ID: {self.__payment_id} | Date: {self.__payment_date} | "
                f"Amount: ${self.__amount:.2f} | Method: {self.__method}")







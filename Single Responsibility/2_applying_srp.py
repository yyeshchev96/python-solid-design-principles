"""
We can fix that by moving `pay` to be a separate class
"""


class IncorrectPaymentType(Exception):
    pass


# create a seprate class to handle Payment Processing
class PaymentProcessor:
    def pay_debit(self, order):
        pass

    def pay_credit(self, order):
        pass


class Order:
    items = {}
    status = "open"

    def add_item(self, name, quantity):
        if name not in self.items:
            self.items[name] = quantity
        else:
            self.items[name] += quantity

    @property
    def total_price(self):
        pass

    # not Order is not responsible for Payment handling, and pass this operation to be performed
    # in a separate class
    def pay(self, payment_method):
        if payment_method == "debit":
            self.status = PaymentProcessor.pay_debit(self)
        elif payment_method == "credit":
            self.status = PaymentProcessor.pay_credit(self)
        else:
            raise IncorrectPaymentType(f"{payment_method} payment method is not supported")

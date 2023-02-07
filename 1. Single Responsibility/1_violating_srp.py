"""
Single Responsibility: a class should have one and only one reason to change.

But does it mean? - There are number of definitions, but in general we should think about Users (who will use this class) as of Actors
So you should design your class in such a way, that it can be used only by ONE, SPECIFIC Actor.

Let's look at the example where class violates SRP principle
"""


class IncorrectPaymentType(Exception):
    pass


class Order:
    items = {}
    status = "open"

    def add_item(self, name, quantity):
        if name not in self.items:
            self.items[name] = quantity
        else:
            self.items[name] += quantity

    def pay(self, payment_method):
        if payment_method == "debit":
            # handle debit payment type
            pass
        elif payment_method == "credit":
            # handle credit payment type
            pass
        else:
            raise IncorrectPaymentType(f"{payment_method} payment method is not supported")


"""
class Order is responsible for managing order and processing payment. 
Also, it should support different payment methods.

so `Order.pay` method violates SRP.
"""

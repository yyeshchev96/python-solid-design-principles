"""
Open-Closed Principle: 

    Objects or entities should be open for extension but closed for modification

It means, that we should be able to easily add any new entities based on the current code
Let's look at the example when this principle is not met:
"""


class Order:
    items = {}
    status = "open"


class PaymentProcessor:
    def pay_debit(self, order: Order):
        pass

    def pay_credit(self, order: Order):
        pass


"""
What if we want to add a new payment method? So we need to write additional methods...
It might be an easy task, but in other places of program you will need so if-else blocks
to support this logic, which will make our code hard to maintain 
"""

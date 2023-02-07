"""
Applying Open-Closed Principle

In this example we will apply OCP to make our class extendable.
This is done by creating a new layer of abstraction
"""

# abc stands for Abstract Base Class (you might see similar things in Java code)
from abc import ABC, abstractmethod


class BasePaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        """Implement payment logic for new Payment method"""
        raise NotImplementedError("Method is not implemented")


# now we can use this base class to implement any payment method:


class DebitPaymentProcessor(BasePaymentProcessor):
    def pay(self, order):
        print("using debit payment method")


class CreditPaymentProcessor(BasePaymentProcessor):
    def pay(self, order):
        print("using credit payment method")


debit_processor = DebitPaymentProcessor()
debit_processor.pay("")

credit_processor = CreditPaymentProcessor()
credit_processor.pay("")

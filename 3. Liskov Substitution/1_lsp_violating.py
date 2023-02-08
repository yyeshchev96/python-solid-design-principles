"""
Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable 
with objects of its subclasses without breaking the application. 

In other words, what we want is to have the objects of our subclasses 
behaving the same way as the objects of our superclass.
"""
import logging
from abc import ABC, abstractmethod


class BasePaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        """Implement payment logic for new Payment method"""
        raise NotImplementedError("Method is not implemented")


class DebitPaymentProcessor(BasePaymentProcessor):
    """Pay using Debit bank card"""

    def pay(self, order, security_code):
        # some logic to do payment using Debit card
        logging.debug(f"Checking security code: {security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(BasePaymentProcessor):
    """Pay using Paypal"""

    # according to BasePaymentProcessor.pay, we need to provide security_code
    # but Paypal actually needs an "email" instead
    def pay(self, order, email: str):
        # some logic to do payment using Paypal

        # so here we're violating LSP
        logging.debug(f"Oh, wait, we don't need a security code, we need an email! {email}")
        order.status = "paid"

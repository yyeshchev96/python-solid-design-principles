"""
In order to solve this problem, we need to make BasePaymentProcessor class more "abstract",
so each child class can extend in and add required attributes for a specific Payment method
"""
import logging
from abc import ABC, abstractmethod


class BasePaymentProcessor(ABC):
    @abstractmethod
    # CHANGES: we removed "security_code" from attributes
    def pay(self, order):
        raise NotImplementedError("Method is not implemented")


class DebitPaymentProcessor(BasePaymentProcessor):
    """Pay using Debit bank card"""

    # CHANGES: security_code has been moved to init method
    def __init__(self, security_code: int) -> None:
        self._security_code = security_code

    # CHANGES: now we can implement pay() method and also use _security_code set in init previosly
    def pay(self, order):
        logging.debug(f"Checking security code: {self._security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(BasePaymentProcessor):
    """Pay using Paypal"""

    # CHANGES: moved email to init and made it protected
    def __init__(self, email: str) -> None:
        self._email = email

    def pay(self, order):
        # some logic to do payment using Paypal
        logging.debug(
            f"Now we can use custom logic for Paypal method without violating LSP: {self._email}"
        )
        order.status = "paid"

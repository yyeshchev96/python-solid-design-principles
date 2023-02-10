"""
Interface Segregation - clients should not be forced to depend on methods that they do not use.

If there are some exra methods in abstraction/interface - thing about classes which will use it.
Maybe would be better to create a separate class which will be responsible for this extra logic.
"""

import logging
from abc import ABC, abstractmethod


class BasePaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        raise NotImplementedError("Method is not implemented")

    @abstractmethod
    def sms_auth(self, order_id):
        raise NotImplementedError("Method is not implemented")


class DebitPaymentProcessor(BasePaymentProcessor):
    """Pay using Debit bank card"""

    def __init__(self, security_code: int) -> None:
        self._security_code = security_code

    def pay(self, order):
        pass

    # Debit payment method has sms_auth, so it will be implemented
    def sms_auth(self, order_id):
        logging.info(f"Using 3D Secure for order: {order_id}")


class ApplePayPaymentProcessor(BasePaymentProcessor):
    """Pay using ApplePay"""

    def pay(self, order):
        pass

    # ISSUE: ApplePay doesn't have sms_auth, but we're forced to implement it (somehow)
    # We violated ISP since we have to provide an implementation for method we're not planning to use
    def sms_auth(self, order_id):
        # by raising an exceptions we violated LSP as well
        raise Exception("sms_auth() method can'y be used with ApplePay")

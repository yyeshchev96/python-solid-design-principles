"""
It's a good idea to move unique class capabilities into a separate interface

For languages like Java, it will mean that we don't have to recompile the code
in case something changes on a child classes
"""

import logging
from abc import ABC, abstractmethod


class BasePaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        raise NotImplementedError("Method is not implemented")


# CHANGES: we moved sms_auth into a separate class, so we now have more flexability
# NOTE: There is a better way, but we've leavee it for DIP section
class SMSAuthPaymentProcessor(BasePaymentProcessor):
    def sms_auth(self, order_id):
        logging.info(f"Using 3D Secure for order: {order_id}")


# CHANGES: Debit can inherit SMSAuth class since it has sms_auth() functionality
class DebitPaymentProcessor(SMSAuthPaymentProcessor):
    """Pay using Debit bank card"""

    def __init__(self, security_code: int) -> None:
        self._security_code = security_code

    def pay(self, order):
        pass


# ApplePay doesn't have sms_auth functionality, so it should inherit base PaymentProcessor
# so now we're following ISP: clients should not be forced to depend on methods that they do not use
class ApplePayPaymentProcessor(BasePaymentProcessor):
    """Pay using ApplePay"""

    def pay(self, order):
        pass

    # CHANGES: now we do not need to implement sms_auth :)

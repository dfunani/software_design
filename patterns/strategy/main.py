from abc import ABC, abstractmethod

# Define the Payment Behavior Interface:
class IPaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Implement Concrete Payment Strategies:
class CreditCardPayment(IPaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(IPaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class CryptoPayment(IPaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Cryptocurrency")

# Create the Context Class (PaymentProcessor):
class PaymentProcessor:
    def __init__(self, payment_strategy: IPaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: IPaymentStrategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        self.payment_strategy.pay(amount)

# Initialize with a Credit Card payment strategy
payment_processor = PaymentProcessor(CreditCardPayment())
payment_processor.process_payment(100)  # Output: Paid 100 using Credit Card

# Change to PayPal payment strategy
payment_processor.set_payment_strategy(PayPalPayment())
payment_processor.process_payment(200)  # Output: Paid 200 using PayPal

# Change to Cryptocurrency payment strategy
payment_processor.set_payment_strategy(CryptoPayment())
payment_processor.process_payment(300)  # Output: Paid 300 using Cryptocurrency
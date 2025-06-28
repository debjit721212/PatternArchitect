class PayPal:
    def paypal_send(self, amount):
        print(f"Paid {amount} using PayPal.")

class Stripe:
    def stripe_charge(self, amount):
        print(f"Charged {amount} using Stripe.")

class Bitcoin:
    def send_crypto(self, amount):
        print(f"Sent {amount} BTC.")


class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError

class PaymentAdapter(PaymentProcessor):
    def __init__(self, payment_service):
        self.payment_service = payment_service

    # def process_payment(self, amount):
    #     # You will write logic here to call correct method
    #     if isinstance(self.payment_service,PayPal):
    #         self.payment_service.paypal_send(amount=amount)
    #     elif isinstance(self.payment_service,Stripe):
    #         self.payment_service.stripe_charge(amount=amount)
    #     elif isinstance(self.payment_service,Bitcoin):
    #         self.payment_service.send_crypto(amount=amount)
    def process_payment(self, amount):
        if hasattr(self.payment_service, 'paypal_send'):
            self.payment_service.paypal_send(amount)
        elif hasattr(self.payment_service, 'stripe_charge'):
            self.payment_service.stripe_charge(amount)
        elif hasattr(self.payment_service, 'send_crypto'):
            self.payment_service.send_crypto(amount)

if __name__ == "__main__":
    amount = 100

    paypal_adapter = PaymentAdapter(PayPal())
    stripe_adapter = PaymentAdapter(Stripe())
    bitcoin_adapter = PaymentAdapter(Bitcoin())

    paypal_adapter.process_payment(amount)
    stripe_adapter.process_payment(amount)
    bitcoin_adapter.process_payment(amount)
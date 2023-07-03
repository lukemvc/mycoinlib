import uuid

class MyCoin:
    def __init__(self, crypto_class):
        self.crypto_class = crypto_class

    def generate_invoice_number(self):
        invoice_number = str(uuid.uuid4())
        return invoice_number
    
    def create_order(self, amount: float):
        invoice_number = self.generate_invoice_number()
        wallet = self.crypto_class.create_wallet()
        crypto_amount = self.crypto_class.usd_to_crypto(amount)

        order_info = {
            'invoice_number': invoice_number,
            'crypto_amount': crypto_amount,
            'wallet': wallet,
        }
        return order_info
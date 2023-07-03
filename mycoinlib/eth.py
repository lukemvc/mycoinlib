
import requests
from eth_account import Account
from eth_keys import keys
from eth_utils import decode_hex

class ETH:
    # Create a new ETH wallet
    def create_wallet():
        account = Account.create()
        private_key = account._private_key.hex()
        priv_key_bytes = decode_hex(private_key)
        priv_key = keys.PrivateKey(priv_key_bytes)
        pub_key = priv_key.public_key
        address = pub_key.to_checksum_address()
        public_key = str(pub_key)
        info = {
            'crypto_type': 'ETH',
            'private_key': private_key,
            'public_key': public_key,
            'wallet_address': address
        }
        return info


    # retrieve current ETH price
    @staticmethod
    def current_price():
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        try:
            r = requests.get(url)
            r.raise_for_status()  
            data = r.json()
            usd = data.get('ethereum').get('usd')
            return float(usd)
        
        except (requests.RequestException, ValueError, KeyError) as e:
            raise APIException("Failed to retrieve ETH price from the API.") from e


    # convert USD to ETH
    @staticmethod
    def usd_to_crypto(amount: float):
        try:
            current_price = ETH.current_price()
            eth_amount = amount / current_price
            formatted_eth_amount = format(eth_amount, ".6f")
            return float(formatted_eth_amount)
        except APIException as e:
            raise APIException("Failed to convert USD to ETH.") from e


    # get confirmed ETH balance
    def get_confirmed_balance(wallet: str):
        url = f"https://api.blockcypher.com/v1/eth/main/addrs/{wallet}/balance"
        try:
            r = requests.get(url)
            r.raise_for_status() 
            data = r.json()
            wei = data.get('balance')
            eth = wei / 10 ** 18
            return float(eth)
        except (requests.RequestException, ValueError, KeyError) as e:
            raise APIException("Failed to retrieve confirmed ETH balance.") from e
        
class APIException(Exception):
    pass
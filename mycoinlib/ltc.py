from bitcoinlib.keys import HDKey
import requests

class LTC:
    def create_wallet():
        key = HDKey(network='litecoin')
        private_key = key.wif()
        public_key = key.public_hex
        address = key.address()
        info = {
            'crypto_type': 'LTC',
            'private_key': private_key,
            'public_key': public_key,
            'wallet_address': address
        }
        return info


    def current_price():
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd"
            r = requests.get(url)
            r.raise_for_status()  # Raise exception for non-2xx status codes
            data = r.json()
            ltc = data.get('litecoin').get('usd')
            return float(ltc)
        
        except (requests.RequestException, ValueError, KeyError) as e:
            raise APIException("Failed to retrieve ETH price from the API.") from e


    def usd_to_crypto(amount: float):
        try:
            current_price = LTC.current_price()
            ltc_amount = amount / current_price
            formatted_ltc_amount = format(ltc_amount, ".6f")
            return float(formatted_ltc_amount)
        
        except APIException as e:
            raise APIException("Failed to convert USD to LTC.") from e


    def get_confirmed_balance(wallet: str):
        url = f"https://api.blockcypher.com/v1/ltc/main/addrs/{wallet}/balance"
        try:
            r = requests.get(url)
            r.raise_for_status()  # Raise exception for non-2xx status codes
            data = r.json()
            balance_litoshis = data.get('balance')
            ltc = balance_litoshis / 100000000
            return float(ltc)
        except (requests.RequestException, ValueError, KeyError) as e:
            raise APIException("Failed to retrieve confirmed LTC balance.") from e
        
class APIException(Exception):
    pass

from bitcoinlib.keys import HDKey
import blockcypher
import requests

class BTC:
    def create_wallet():
        key = HDKey(network='bitcoin')
        private_key = key.wif()
        public_key = key.public_hex
        address = key.address()
        info = {
            'crypto_type': 'BTC',
            'private_key': private_key,
            'public_key': public_key,
            'wallet_address': address
        }
        return info


    def current_price():
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
            usd = data.get('bitcoin').get('usd')
            return float(usd)
        except (requests.RequestException, ValueError, KeyError) as e:
            raise APIException("Failed to retrieve BTC price from the API.") from e


    def usd_to_crypto(amount: float):
        try:
            current_price = BTC.current_price()
            btc_amount = amount / current_price
            formatted_btc_amount = format(btc_amount, ".6f")
            return float(formatted_btc_amount)
        
        except APIException as e:
            raise APIException("Failed to convert USD to BTC.") from e


    # get confirmed BTC balance of wallet
    def get_confirmed_balance(wallet: str):
        url = f"https://api.blockcypher.com/v1/btc/main/addrs/{wallet}/balance"
        try:
            data = requests.get(url).json()
            sats = data.get('balance')
            btc = blockcypher.from_base_unit(sats, 'btc')
            return float(btc)
        
        except APIException as e:
            raise APIException("Failed retrieve confirmed BTC balance") from e
        

class APIException(Exception):
    pass

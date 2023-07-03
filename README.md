# MyCoinLib Documentation

## Overview

MyCoinLib is a Python package for generating unique BTC, LTC, and ETH wallet/private-key pairs for customer orders, along with other related functions.

## Installation
```python
pip install mycoinlib
```
Upgrade using 
```python
pip install --upgrade mycoinlib
```

## Usage

To use mycoinlib, import the necessary modules for your use case.

```python
from mycoinlib import MyCoin, BTC, LTC, ETH
```

Start by instanciating MyCoin with the desired crypto class.

```python
mycoin = MyCoin(BTC)
```
Then pass the order amount to the create_order function in USD, and it will include the converted crypto amount in the response.

```python
usd_amount = 24.99
wallet_info = mycoin.create_order(usd_amount)
print(wallet_info)
```
Output
```
{
    'invoice_number': 'fe48e080-7972-4571-bf00-dd224efcfeec',
    'crypto_amount': 0.000801,
    'wallet': {
        'crypto_type': 'BTC',
        'private_key': 'xpub661MyMwAqRbcFA1vyZxC21eKQ75K4xeCu86vhQkzURptK3BJXR7fTysmtPPdKot4ViHyhiQZ7YfzuaNjN2p31fbHMF7vsJ1ZT1ZucfkySo5',
        'public_key': '036252c9bc74089b4f0856b3161fa200ac7f804e2b3439c410db16a5ae2ef9686e',
        'wallet_address': '11J4ijkhppHn5AziqwGXfpKAboFSCo5iH'
    }
}

```
The process is the same for ETH and LTC.

```python
mycoin = MyCoin(ETH)
usd_amount = 24.99
wallet_info = mycoin.create_order(usd_amount)
print(wallet_info)
```
Output
```
{
    'invoice_number': '02b83d59-d258-4ca1-bc59-046abb3ca2f2',
    'crypto_amount': 0.012681,
    'wallet': {
        'crypto_type': 'ETH',
        'private_key': '0xee5d0e9fce90b05b298d42f5a0b54bfb690819ace38c361bae07e934585ec729',
        'public_key': '0xc565011779960aa8424ff71fe04fcd531a095dc5785815ae6863500eedbc17b10e063e651e8c740272a5b711b36acbd0fee93501a628425eb6f0596918da846f',
        'wallet_address': '0x5E65828A2aEE3B722a40fE5620A5Cf776323212a'
    }
}
```

## Additional Functions

Each crypto class (BTC, LTC, ETH) has additional functions that can be used without instanciating MyCoin
<br></br>

### Get Confirmed Balance 
Retrieve the current confirmed balance of a wallet by passing the wallet to the get_confirmed_balance function. This will return the wallets current confirmed balance as a floating point number.

```python
balance = BTC.get_confirmed_balance(btc_wallet)
balance = LTC.get_confirmed_balance(ltc_wallet)
balance = ETH.get_confirmed_balance(eth_wallet)
```
<br>

### Get Current Price
Retrieve the current price of a crypto by using the following functions.
```python
current_btc_price = BTC.current_price()
current_ltc_price = LTC.current_price()
current_eth_price = ETH.current_price()
```
<br>

### Convert USD to Crypto
You can convert an amount in USD to the corresponding amount in the respective cryptocurrency.

```python
usd_amount = 420.69

btc_amount = BTC.usd_to_crypto(usd_amount)
ltc_amount = LTC.usd_to_crypto(usd_amount)
eth_amount = ETH.usd_to_crypto(usd_amount)
```

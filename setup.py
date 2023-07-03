from setuptools import setup

setup(
    name='mycoinlib',
    version='0.0.2',
    description='A Python package for generating unique BTC, LTC, and ETH wallets for customer orders',
    long_description='MyCoinLib is a Python package for generating unique BTC, LTC, and ETH wallet/private-key pairs for customer orders, along with other related functions.',
    url='https://github.com/lukemvc/mycoinlib',
    packages=['mycoinlib'],
    install_requires=[
        'bitcoinlib',
        'blockcypher',
        'requests',
        'eth_account',
        'eth-keys',
    ]
)

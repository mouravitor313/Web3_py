import json
from web3 import Web3

infura_url = 'https://sepolia.infura.io/v3/a9cf406c2afd48c6a66900188b8e0254'
web3 = Web3(Web3.HTTPProvider(infura_url))
balance = web3.from_wei(web3.eth.get_balance('0x3e789E581376A54Fc1032f61EEE758D5F8C68949'), 'ether')
print(web3.is_connected(), web3.eth.block_number, balance)
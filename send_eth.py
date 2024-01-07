from web3 import Web3
from scripts.ganache_script import *

account_1 = '0x9225d91F9e1E62257599deEC541a8BC37C0c2498'
account_2 = '0xb1ecDAb73DfF9211Ef7702B17869D25Bb78BB0eE'

nonce = web3.eth.get_transaction_count(account_1)

tx = {
    'nonce':nonce,
    'to': account_2,
    'value':web3.to_wei(1, 'ether'),
    'gas':200000,
    'gasPrice': web3.to_wei('50', 'gwei')
}

# Assine a transação
signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

# Obtenha a transação assinada em formato de bytes
raw_tx = signed_tx.rawTransaction

# Envie a transação assinada
tx_hash = web3.eth.send_raw_transaction(raw_tx)

print(tx_hash)



import os
from web3 import Web3

# Connect to the Ethereum network
infura_url = "https://sepolia.infura.io/v3/123f156f7b2d494786f6fdd943972123"

# Load sensitive data from environment variables
infura_url = os.getenv('INFURA_URL')
private_key = os.getenv('PRIVATE_KEY')

web3 = Web3(Web3.HTTPProvider(infura_url))

# Your Ethereum account private
private_key = private_key

# Smart contract address and ABI
contract_address = "0x53358f44cc127dE63dDe5cfe1Cc963168d22c828"

# Your Ethereum account
account = "0x53358f44cc127dE63dDe5cfe1Cc963168d22c828"
test_user_address = "0x53358f44cc127dE63dDe5cfe1Cc963168d22c828"


abi = '''
[
    {
        "constant": false,
        "inputs": [
            {
                "name": "user",
                "type": "address"
            }
        ],
        "name": "authenticate",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "user",
                "type": "address"
            }
        ],
        "name": "isAuthenticated",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
'''

contract = web3.eth.contract(address=contract_address, abi=abi)



def authenticate_user(user_address):
    nonce = web3.eth.get_transaction_count(account)
    txn = contract.functions.authenticate(user_address).build_transaction({
        'chainId': 4,  # Rinkeby Testnet
        'gas': 200000,
        'gasPrice': web3.to_wei('2', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash.hex()

# Authenticate a test user
tx_hash = authenticate_user(test_user_address)
print(f'Authenticated {test_user_address} with transaction hash: {tx_hash}')

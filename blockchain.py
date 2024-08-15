from web3 import Web3
import os

infura_url = os.getenv("INFURA_URL")

# Connect to the Ethereum network
infura_url = infura_url

web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected to the blockchain
if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect to Ethereum network")

# Smart contract address and ABI
contract_address = "0x53358f44cc127dE63dDe5cfe1Cc963168d22c828"
abi = '''
[
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

def is_user_authenticated(user_address):
    try:
        return contract.functions.isAuthenticated(user_address).call()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

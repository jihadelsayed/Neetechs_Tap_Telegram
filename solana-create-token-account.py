import json
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.rpc.types import TxOpts
from solders.keypair import Keypair
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import create_associated_token_account, get_associated_token_address

# Function to get the public key from a Keypair
def get_public_key_from_keypair():
    keypair = Keypair()
    public_key = keypair.pubkey()
    print(f"Public Key: {public_key}")
    return keypair, public_key

# Function to derive a public key from a seed phrase
def get_public_key_from_seed(seed_phrase):
    seed = seed_phrase.encode('utf-8')
    keypair = Keypair.from_seed(seed[:32])
    public_key = keypair.pubkey()
    print(f"Derived Public Key: {public_key}")
    return keypair, public_key

# Prompt the user for their seed phrase
seed_phrase = input("Please enter your seed phrase: ")

# Get and print public keys
keypair, public_key = get_public_key_from_keypair()
derived_keypair, derived_public_key = get_public_key_from_seed(seed_phrase)

# Save the derived public key to a JSON file
wallet_json = {
    "pubkey": str(derived_public_key)
}

with open('my-solana-wallet.json', 'w') as json_file:
    json.dump(wallet_json, json_file)

print("Wallet JSON file 'my-solana-wallet.json' created.")

# Solana client setup
client = Client("https://api.mainnet-beta.solana.com")

# Token address (replace with your actual token address)
token_address = PublicKey("DzmiPvaaPBFHwqencRn7otWzJi44RkRFR3YaQz88Diuk")

# Function to create a token account
def create_token_account(owner_keypair, token_address):
    # Derive the associated token account address
    associated_token_account = get_associated_token_address(owner_keypair.pubkey(), token_address)

    # Create associated token account instruction
    transaction = Transaction()
    transaction.add(create_associated_token_account(
        payer=owner_keypair.pubkey(),
        owner=owner_keypair.pubkey(),
        mint=token_address
    ))

    # Send transaction
    response = client.send_transaction(transaction, owner_keypair, opts=TxOpts(skip_preflight=True, skip_confirmation=False))
    print(f"Response: {response}")

# Create a token account using the derived keypair
create_token_account(derived_keypair, token_address)

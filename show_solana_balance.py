import solana
from solana.rpc.api import Client
from solana.publickey import PublicKey

# Connect to the Solana cluster
client = Client("https://api.mainnet-beta.solana.com")

# Replace with your Solana public address
public_address = input("Please enter your public address: ")

# Convert the public address to a Pubkey object
pubkey = PublicKey(public_address)

# Fetch balance in lamports
balance_lamports = client.get_balance(pubkey)['result']['value']

# Convert lamports to SOL
balance_sol = balance_lamports / 1_000_000_000

# Print the balance with decimal points
print(f"Balance: {balance_sol:.9f} SOL")

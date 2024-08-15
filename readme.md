pip install mnemonic bip32utils eth_utils
pip install mnemonic bip44 eth-account



# solana 
from solders.hash import Hash as Blockhash
from solders.instruction import AccountMeta, Instruction
from solders.keypair import Keypair
from solders.message import Message
from solders.message import Message as SoldersMessage
from solders.presigner import Presigner
from solders.pubkey import Pubkey
from solders.signature import Signature
from solders.transaction import Transaction as SoldersTx
from solders.transaction import TransactionError
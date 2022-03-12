from hashlib import sha1, sha224, sha256, sha512
from time import gmtime, time

class Block:
	nOnce = 0
	def __init__(self, prev_hash=None, txn=None, timestamp=time()):
		if timestamp is None:
			self.genesis_block = Block(None, None, timestamp)
			self.nOnce = Block.nOnce
		else:
			self.prev_hash = prev_hash
			self.txn = txn
			self.timestamp = timestamp
			self.nOnce = Block.nOnce
		Block.nOnce += 1

genesis_Block = Block()
block_1 = Block(genesis_Block, 100)
block_2 = Block(block_1, 20)
block_3 = Block(block_2, 130)

print(genesis_Block.nOnce, block_1.nOnce, block_2.nOnce, block_3.nOnce, sep='\n')
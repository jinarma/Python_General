from hashlib import sha256, sha1
from time import time

class Block:
	def __init__(self, prev_hash:str, txn:str, timestamp=time()) -> None:
		self.prev_hash = prev_hash
		self.txn = txn
		self.timestamp = timestamp
		self.block_data = str(txn) + '-' + prev_hash
		self.block_hash = sha1(self.block_data.encode()).hexdigest()

class Chain:
	def __init__(self) -> None:
		self.chain = []
		self.generate_genesis()
	
	def generate_genesis(self):
		self.chain.append(Block('aadhar', 0))

	def next_block(self, txn):
		prev_hash = self.last_block.block_hash
		self.txn = txn
		self.chain.append(Block(prev_hash, self.txn))
	
	@property
	def last_block(self) -> Block:
		return self.chain[-1]

	def size_of_chain(self) -> int:
		return len(self.chain)

	def display(self):
		for ele in self.chain:
			print(ele.block_data, ele.block_hash)

test_block = Chain()

for i in range(1, 5):
	test_block.next_block(i)

test_block.display()

print(test_block.size_of_chain())

# print(genesis_Block.prev_hash)
# print(block_1.prev_hash)
# print(block_2.prev_hash)
# print(block_3.prev_hash)
# # print(sha256('0'.encode()).hexdigest())

# # print(f'genesis_block.prev_hash {genesis_Block.prev_hash}, genesis_Block.txn {genesis_Block.txn}, genesis_Block.timestamp {genesis_Block.timestamp}, genesis_Block.number {genesis_Block.number}')
# # print(f'block_1.prev_hash {block_1.prev_hash}, block_1.txn {block_1.txn}, block_1.timestamp {block_1.timestamp}, block_1.number {block_1.number}')




# a = 'sup'
# b = 'soup'

# c = sha256(a.encode()).hexdigest() + sha256(b.encode()).hexdigest()
# # print(sha256(c.encode()).hexdigest())

from hashlib import sha1, sha224, sha256, sha512

class Block:
	def __init__(self, prev_hash=None, txn_root=None, timestamp=None, nOnce=None):
		if prev_hash is None:
			genesis_block = Block()
	
	def current_txn_hash(txn_list):
		for txn in txn_list:
			txn_list

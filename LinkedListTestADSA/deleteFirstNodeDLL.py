class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DLL:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			t = self.head
			while t is not None:
				t = t.next
			t = new_node

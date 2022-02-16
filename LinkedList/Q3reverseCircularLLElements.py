class Node:
	def __init__(self, data):
		self.dat = data
		self.next = None
		self.prev = None

class DCLL:
	def __init__(self):
		self.head = None

	def insert_next(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			t = self.head
			while t.next != self.head:
				t = t.next
			t.next = node
			
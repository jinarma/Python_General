class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DLL:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def insert_next(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			t = self.head
			while t.next is not None:
				t = t.next
			t.next = node
			t.next.prev = t
			self.tail = node

	def display_all(self):
		if self.head == None:
			print(None)
		else:
			t = self.head
			while t is not None:
				print(t.data, end = ' ')
				t = t.next
	def display_rev(self):
		if self.tail == None:
			print(None)
		else:
			t = self.tail
			while t is not None:
				print(t.data, end = ' ')
				t = t.prev


if __name__ == '__main__':
	a = DLL()
	a.insert_next(2)
	a.insert_next(4)
	a.insert_next(6)
	a.display_all()
	print()
	a.display_rev()
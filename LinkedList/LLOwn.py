# SLL

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SLL:
	head = None

	def insert_at_end(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			t = self.head
			while t.next is not None:
				t = t.next
			t.next = node
	
	def display_all(self):
		if self.head == None:
			print(None)
		else:
			t = self.head
			while t is not None:
				print(t.data, end = ' ')
				t = t.next

if __name__ == '__main__':
	a = SLL()
	a.insert_at_end(2)
	a.insert_at_end(4)
	a.insert_at_end(6)
	a.display_all()
	print()
	b = SLL()
	b.insert_at_end(1)
	b.insert_at_end(3)
	b.insert_at_end(5)
	b.display_all()

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class SL():
	def __init__(self):
		self.head = None
		self.tail = None
	
	def insert(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
		else:
			t = self.head
			while t.next is not None:
				t = t.next
			t.next = new_node
		

	def display_entire(self):
		t = self.head
		while t is not None:
			print(t.data)
			t = t.next
a = SL()
a.insert(10)
a.insert(20)
a.insert(40)
a.insert(700)
a.display_entire()
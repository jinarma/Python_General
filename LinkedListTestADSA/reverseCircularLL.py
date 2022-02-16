# Incomplete

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DCLL:
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			self.head.next = new_node
			self.head.prev = new_node
		else:
			t = self.head
			print(f"t = {t}\nt.next.next = {t.next.next.data}\nself.head = {self.head}")
			# print('\n'*3)
			while True:
				if t.next == self.head:
					t.next = new_node
					t.next.prev = t
					t = t.next
					t.next = self.head
					self.head.prev = t
					print('sup')
					break
				elif t.next != self.head:
					t = t.next
					# print(f"t.next = {t.next}\nself.head = {self.head}")

	def display_all(self):
		t = self.head
		if t == None:
			print(None)
		else:
			print(t.data)
			t = t.next
			while t != self.head.next:
				print(t.data)
				t = t.next


def main():
	a = DCLL()
	uselessInp = 4
	ls = [20, 12, 34, 12, 18]
	for i in ls:
		a.insert(i)
	a.display_all()

main()

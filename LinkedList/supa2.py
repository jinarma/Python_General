class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SLL:
	def __init__(self):
		self.head = None
		#self.next = None
		self.insert_at_end(num_list)

	def insert_at_end(self, num_list):
		for i in num_list:
			if (self.head == None):
				self.head = Node(i)
			else:
				current = self.head
				while current.next != None:
					current = current.next
				current.next = Node(i)

	def display_all(self):
		temp = self.head
		if temp == None:
			print("None")
		else:
			while temp.next != None:
				print(temp.data)
				temp = temp.next
			print(temp.data)


size_of_list = int(input())
num_list = list(map(int, input().split()))
posi = int(input())

linked_list = SLL()
# linked_list.display_at_posi(posi)
linked_list.display_all()

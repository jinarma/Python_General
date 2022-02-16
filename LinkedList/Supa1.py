#3
#6 10 12
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
			
	# def display_at_middle(self, N):
	# 	temp = self.head
	# 	if temp == None:
	# 		print("None")
	# 	else:
	# 		posi = N
	# 		while posi != N//2 + 1:
	# 			temp = temp.next
	# 			posi -= 1 
	# 		print(temp.data, end = " ")
	# 		if N%2 == 0:
	# 			print(temp.next.data)


size_of_list = int(input())
num_list = list(map(int, input().split()))

linked_list = SLL()
linked_list.display_all()
# linked_list.display_at_middle(size_of_list)
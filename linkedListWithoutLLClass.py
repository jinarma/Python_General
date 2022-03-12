class Node:
	def __init__(self, data = None, previous_node_address = None):
		if previous_node_address is None and data is None:
			self.genesis_node = Node(None, None)
		self.data = data
		self.previous_node_address = previous_node_address
	

def main():
	genesis_node = Node()
	node2 = Node(10, genesis_node)
	node3 = Node(20, node2)
	print(f'node3.data = {node3.data}, node3 address = {node3}, node3.prevous_address = {node3.previous_node_address}')
	print(f'node2.data = {node2.data}, node2 address = {node2}, node2.prevous_address = {node2.previous_node_address}')
	print(f'genesis_node.data = {genesis_node.data}, genesis_node address = {genesis_node}, genesis_node.prevous_address = {genesis_node.previous_node_address}')
	print('\n\n\n\n')
	genesis_node2 = Node()
	ls1 = []
	for i in range(5):
		if i == 0:
			ls1.append(genesis_node2)
			temp = genesis_node2
		else:
			data = i*10
			previous = temp
			temp2 = Node(data, previous)
			temp = temp2
	print(temp2.data)
	print(temp2.previous_node_address.data)
	print(temp2.previous_node_address.previous_node_address.data)
	print('\n\n\n\n')
	current_node = temp2
	index = 0
	while current_node is not None:
		print(f'{index} current_node.data = {current_node.data}, current_node address = {hex(id(current_node))}, current_node.previous_node_address = {current_node.previous_node_address}')
		index -= 1
		current_node = current_node.previous_node_address
main()

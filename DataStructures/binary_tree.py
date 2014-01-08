# implementing binary tree in python

class Node:

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self, data):

		if data < self.data:
			if not self.left:
				self.left = Node(data)
			else:
				self.left.insert(data)
		elif data > self.data:
			if not self.right:
				self.right = Node(data)
			else:
				self.right.insert(data)

	def lookup(self, data):
		if self.data == data:
			return self.data

		if data < self.data:
			if not self.left:
				return None
			return self.left.lookup(data)
		elif data > self.data:
			if not self.right:
				return None
			return self.right.lookup(data)

root = Node(8)
root.insert(3)
root.insert(10)

my_data = 4

after_find = root.lookup(my_data)

if after_find is None:
	print '%s does not exist in this tree!' % my_data
else:
	print 'Found %s!' % after_find
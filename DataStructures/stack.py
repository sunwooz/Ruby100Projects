class Stack(object):

	#push, pop
	def __init__(self, array=None):
		self.array = []

	def push(self, item):
		self.array.append(item)

	def pop(self):
		popped = self.array[-1]
		del self.array[-1]
		return popped


stack = Stack()

stack.push('monkey')
stack.push('cheese')
stack.push('man')

print stack.pop()
print stack.array
print stack.pop()
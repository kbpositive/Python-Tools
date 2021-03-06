class Node:
	def __init__(self, parent=None, val=0, left=None, right=None):
		self.parent = parent
		self.val = val
		self.left = left
		self.right = right
		self.height = 0
		self.bf = 0


class Tree:
	def __init__(self):
		self.root = None
		self.size = 0
		self.func = lambda x: print(x.val)

	def update(self, node):
		lh = -1
		rh = -1
		if node.left:
			lh = node.left.height
		if node.right:
			rh = node.right.height
		node.height = 1 + max([lh, rh])
		node.bf = rh - lh

	def rotate(self, child, direction: str):
		if direction == 'right':
			parent = child.left
			child.left = parent.right
			parent.right = child
			self.update(child)
			self.update(parent)
			return parent
		elif direction == 'left':
			parent = child.right
			child.right = parent.left
			parent.left = child
			self.update(child)
			self.update(parent)
			return parent

	def case(self, case_type: str, node):
		if case_type == 'll':
			return self.rotate(node, 'right')
		elif case_type == 'lr':
			node.left = self.rotate(node.left, 'left')
			return self.case('ll', node)
		elif case_type == 'rr':
			return self.rotate(node, 'left')
		elif case_type == 'rl':
			node.right = self.rotate(node.right, 'right')
			return self.case('rr', node)

	def balance(self, node):
		if node.bf < -1:
			if node.left.bf <= 0:
				return self.case('ll', node)
			else:
				return self.case('lr', node)
		elif node.bf > 1:
			if node.right.bf >= 0:
				return self.case('rr', node)
			else:
				return self.case('rl', node)
		return node

	def insert_node(self, item, node):
		if node is None:
			return Node(None, item, None, None)
		else:
			if item is node.val:
				return node
			elif node.val < item:
				node.right = self.insert_node(item, node.right)
				node.right.parent = node
				self.size += 1
			else:
				node.left = self.insert_node(item, node.left)
				node.left.parent = node
				self.size += 1
		self.update(node)
		return self.balance(node)

	def insert(self, item):
		self.root = self.insert_node(item, self.root)

	def remove_node(self, item, node):
		if not node:
			return node
		elif node.val > item:
			node.left = self.remove_node(item, node.left)
		elif node.val < item:
			node.right = self.remove_node(item, node.right)
		else:
			if node.left is None:
				temp = node.right
				node = None
				self.size -= 1
				return temp
			elif node.right is None:
				temp = node.left
				node = None
				self.size -= 1
				return temp
			temp = node.right
			while temp.left is not None:
				temp = temp.left
			node.val = temp.val
			node.right = self.remove_node(temp.val, node.right)
			self.size -= 1
		self.update(node)
		return self.balance(node)

	def remove(self, item):
		self.remove_node(item, self.root)

	def traverse_tree(self, node, order):
		if node is None:
			return None
		if order == 'pre':
			self.func(node)
		self.traverse_tree(node.left, order)
		if order == 'in':
			self.func(node)
		self.traverse_tree(node.right, order)
		if order == 'post':
			self.func(node)

	def traversal(self, order='in'):
		self.traverse_tree(self.root, order)

	def find_node(self, item, node=None):
		if node is None:
			raise ValueError('Item not found.')
		elif node.val != item:
			if item < node.val:
				return self.find_node(item, node.left)
			else:
				return self.find_node(item, node.right)
		else:
			return node

	def find(self, item):
		return self.find_node(item, self.root)

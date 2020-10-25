"""
	Node Depths
	Returns the sum of depths (heights) of EVERY node

"""
def nodeDepths(root):
    """
	MAIN IDEA: use DFS! and add the depth to the stack's object AND node
	
	stack = [(root, 0)]	
	"""
	curr_sum = 0
	stack = [(root, 0)]	
	
	while stack:
		node, curr_depth = stack.pop()
		if not node:
			continue # skips and goes to beginning
		curr_sum += curr_depth
		stack.append( (node.left, curr_depth+1) )
		stack.append( (node.right, curr_depth+1) )
	print(curr_sum)
	return curr_sum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

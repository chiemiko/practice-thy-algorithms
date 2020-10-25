class MinMaxStack:
	"""
	def of minmaxstack - can do the following
		push(x) -- Push element x onto stack.
		pop() -- Removes the element on top of the stack.
		top() -- Get the top element.
		getMin() -- Retrieve the minimum element in the stack.
		getMax() -- Retrieve the maximum element in the stack.
	
	MAIN IDEA: need to somehow store min and maxes simulataneously
	
		store the raw data and 'processed' data which involves
		list of tuples (currmin, currmax) at every point! 
	
	"""
	def __init__(self):
		self.minmaxes = [] # ex: [(1, 2), (2, 2), (currmin, currmax)]
		self.stack = []
		
    def peek(self):
        # Write your code here.
        return self.stack[len(self.stack)-1]
		
    def pop(self):
		self.minmaxes.pop()
        return self.stack.pop()
	
    def push(self, number):
        # tricky part
		if len(self.minmaxes):
			new_min =min(self.minmaxes[len(self.stack)-1][0], number)
			new_max = max(self.minmaxes[len(self.stack)-1][1], number)
		else:
			new_min, new_max = number, number
		self.minmaxes.append( (new_min, new_max) )
        self.stack.append(number)

    def getMin(self):
        return self.minmaxes[len(self.stack)-1][0]

    def getMax(self):
		return self.minmaxes[len(self.stack)-1][1]
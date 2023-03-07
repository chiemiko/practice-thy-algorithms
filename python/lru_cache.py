"""
4:02 

GOAL: 
LRUCache: 
	insertKeyValuePair
	getValueFromKey
	getMostRecentKey
constraint: maxsize 

Main idea: -> USE POINTERS AND REARRANGE THINGS INSTEAD OF SHIFTING ALOT OF DATA

	need to use a combination of both hash map and linked list pointers
	in order to 
		1. access in constant time and 
		2. deal with the weird reordering 

use a hashset and a separate pointers with the keys of the hashset 

steps:
1. need to create the class components... 
	head/tail of doubly linked list with keys as nodes 
	dictionaries 

"""
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
		self.keyvaluepairs = {}
		self.currlen = len(self.keyvaluepairs)
		self.orderedLL = DoubleLinkedList()
		
    def insertKeyValuePair(self, key, value):
        """
		this is an important one... 
		
		needs to include creation of new Node and 
		updateHead to add it to the linkedlist
		
		"""
		if key not in self.keyvaluepairs:
			nextNode = Node(key, value)
			if self.currlen == self.maxSize:
				
				self.popOldestNode() # eviction of cache
				self.currlen = self.currlen-1
			
			self.keyvaluepairs[key] = nextNode
			self.orderedLL.updateHead(nextNode)
			self.currlen+=1
			
		else:
			"""
			this is an important one...
			
			!!!main idea... the trick is to only update the keyvaluepair 
			store .value attribute in the node... 
			but USE the previous node's prev and next links to 
			remove bindings, relink, and set up at the head
			"""
			self.keyvaluepairs[key].value = value
			self.orderedLL.replaceInOrderWith(self.keyvaluepairs[key])

		# print(self.keyvaluepairs.keys(), self.orderedLL.head.key, self.orderedLL.tail.key)

    def getValueFromKey(self, key):
        """get value like from dictionary
		
				IMPORTANT EDGE CASE BUT PART OF THE PROMPT!!! 
		
			according to the tests... get requests require a 
			complete update in the LL
			
		"""
		res = self.keyvaluepairs[key].value if key in self.keyvaluepairs else None
		if key in self.keyvaluepairs:
			self.orderedLL.replaceInOrderWith(self.keyvaluepairs[key])
		print(self.keyvaluepairs.keys(), self.orderedLL.head.key, self.orderedLL.tail.key)
		return  res

    def getMostRecentKey(self):
        """
		this is where you use doubled LL
		
		"""
		getMostRecent_key = self.orderedLL.head.key		
		return getMostRecent_key
		
	def popOldestNode(self):
		"""
		!!!  IMPORTANT steps
		
		pop the LEAST RECENT / OLDEST nodes 
		then reset the tail of the linkedlist
		
		1. read OLDEST (LRU) node
		2. remove from dict and orderedLL
		3. return?
		"""
		
		tail = self.orderedLL.tail
		
		# remove from keyvaluepair dict
		del self.keyvaluepairs[tail.key]
		
		# remove from linked list
		self.orderedLL.removeTail()
	
class DoubleLinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
	
	def replaceInOrderWith(self, oldnodewithnewval):
		# means the node already exists in the LL... so need to:
		# 1. pop out from middle and
		# 2. add to head
		node = oldnodewithnewval
		print(f'replacing with old new val {node.key}')
		print(f'{node.next.key}')
		print(f'{node.prev.key}')
		if node.prev and node.next:
			node.prev.next = node.next
		elif node.prev:
			self.tail = node.prev
			print('new tail at ', self.tail)
			node.prev.next = None
			
		if node.next:
			node.next.prev = node.prev
				
		node.prev, node.next = None, None		
		self.updateHead(node)
	
	def updateHead(self, node):
		"""
		relink head to new node
		update head
		
		edge cases! 
		if current LL is NONE: set head and tail to be the same 
		"""
		if self.head is None and self.tail is None:
			self.head = node
			self.tail = node
			self.head.next, self.tail.prev = node, node
		else:
			print(node.key)
			self.head.prev = node
			node.next = self.head
			self.head = node
			
	
	def removeTail(self):
		"""
		relink tail node: 
			
			tail.prev.next = None
			LL.tail = tail.prev 			
		"""
		if self.tail is None:
			return
		
		if self.tail == self.head: # THIS CHECK IS IMPORTANT!!! ESPECIALLY WHEN MAXSIZE == 1
			
			self.head, self.tail = None, None
			return		
		print('popping tail here: ', self.tail.key)
		
		self.tail.prev.next = None
		self.tail = self.tail.prev
			
class Node():
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None
		
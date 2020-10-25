def moveElementToEnd(array, target):
	"""
	input = [2, 1, 2, 2, 2, 3, 4, 2]
	target = 2

	Prompt: Write a function that moves all instances of target
	to the end of the array.
	
	MAIN IDEA: aim for O(n) run time! do not sort!
		THERE IS ONE TRICK, where left<right constraint 
		is needed on inner loop to catch quickly changing
		increments
	
		similar to quick sort (pivot sort!)
		two pointers - 
			if array[right] == target
	"""
	# INPLACE sorting method!  O(nlogn)
	array = sorted(array) # nlogn
	left, right = 0, len(array)-1 # logn times to search and find target to move
	
	while left<right:
		while left<right and array[right] == target:
			right-=1
		# MAIN TRICK HERE! USE SWAP to place the target num on left 
		# side to the right side
		if array[left] == target: # O(1) -> MAKE SURE TO INCREMENT LEFT OUTSIDE OF IF 
			array[left], array[right] = array[right], array[left]
		left +=1 
	return array

arr = [2, 1, 2, 2, 2, 3, 4, 2]
target = 2
expected = [1, 4, 3, 2, 2, 2, 2, 2]
if expected == moveElementToEnd(arr, target): print("success")
else: print("Failure")

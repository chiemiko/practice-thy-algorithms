	
def smallestDifference(arr1, arr2):
	"""
	Question:
	
		Given arr1, arr2, find two values from each 
		array where their absolute difference is 
		closest to 0.
	
	MAIN IDEA: use binary search like 2 pointer
	set to iterate from the left of each array.
	
	if any num1 is bigger than num2, increment 
	from that arr1	
	
	TIME COMPLEXITY: O(mlogm) + O(nlogn) because sorting dominates run time
	SPACE COMPLEXITY: O(1) constant time because we're sorting and storing
		evals in place

	"""
	arr1 = sorted(arr1)
	arr2 = sorted(arr2)
	id1, id2 = 0, 0
	
	min_dist = float('inf')
	res = [] # smallest pair
	
	while (id1 < len(arr1)) & (id2 < len(arr2)):
		# update min_dist and res
		curr_dist = abs(arr1[id1]-arr2[id2])
		if min_dist > curr_dist:
			min_dist = curr_dist
			res = [arr1[id1], arr2[id2]]
			
		# evaluate next steps
		if arr1[id1] < arr2[id2]:
			id1+=1
		elif arr1[id1] > arr2[id2]: 
			id2+=1
		else:
			return [arr1[id1], arr2[id2]]
		
	return res

expected = [28, 26]
arr1 = [-1, 5, 10, 20, 28, 3]
arr2 = [26, 134, 135, 15, 17]
if smallestDifference(arr1, arr2) == expected: print("success")
else: print("failure")
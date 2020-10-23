def threeNumberSum(array, targetSum):
	"""
	MAIN IDEA: 
		Hold one "current" idx constant -> and iterate for each to find 
		using BINARY SEARCH the other two pointers who's sum === target
	"""
	array = sorted(array)
	res = []
	for idx in range(len(array)-2):
		l, r = idx+1, len(array)-1
		while l<r:
			# logic
			curr_sum = array[idx] + array[l] + array[r]
			if curr_sum == targetSum:
				res.append([array[idx], array[l], array[r]])
				l+=1
				r-=1
			elif curr_sum > targetSum:
				r-=1
			else:
				l+=1
	return res
		
test_array = [12, 3, 1, 2, -6, 5, -8, 6]
expected_answer = [[-8, 2, 6], [-8, 3, 5],[-6, 1, 5]] 
if expected_answer == threeNumberSum(test_array, 0): print('Success')
else: print('Failure')
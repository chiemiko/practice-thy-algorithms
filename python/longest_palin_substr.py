def longestPalindromicSubstring(string):
	"""
	No alg/special data structure -> trick: do search from middle
    
    input: 'abaxyzzyxf'
			^	
	output: 'xyzzyx'
	
	STEPS: 
	1) define function which iteratively searches from the center outwards
		for valid palindromes
	2) isPalindrome
	3) wrapper iteration to search from idx = [1, 2, 3... len(string)]
	
	"""
	
	length = len(string) # 10
	
	def search_for_palindromes(start, end):
		"""
		TRICKY: 
			in the search for palindromes fx, the exit condition leaves
			EXTRA IDX's in there. So you need to push back in in the return statement. 		
		"""
		while isPalindrome(start, end) and (start>=0) and (end<length):
			start-=1 
			end+=1
		return [start, end+1]
		
	def isPalindrome(start, end):
		search_str = string[start:end+1]
		if search_str == search_str[::-1]:
			print(f'true palindrome: {search_str}')
			print(f'idxs: {start, end+1}')
			return True
		return False
	
	if len(string)<2:
		return string
	curr_longest = [0, 1]
	for idx in range(1, length):
		odd = search_for_palindromes(idx-1, idx)
		even = search_for_palindromes(idx-1, idx+1)
		curr_longest = max(odd, even, curr_longest, key=lambda x: x[1]-x[0])
	
	print(curr_longest[0], curr_longest[1])
	res =  string[curr_longest[0]+1:curr_longest[1]-1]
	print(res)
	return res
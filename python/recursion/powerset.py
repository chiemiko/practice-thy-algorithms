def powerset(array):
    def dfs(res=[], idx=0, curr=[]):
		if len(curr) == k:
			res.append(curr[:])
			print(curr)
			return res
		
		for i in range(idx, len(array)):
			curr.append(array[i])
			dfs(res, i+1, curr)
			curr.pop()
		return res
	
	for k in range(len(array)+1):
		res = dfs()
	return res
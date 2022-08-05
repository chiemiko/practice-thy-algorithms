"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Main Idea: 
    For the base case make sure to set the exit condition to
    be related to the outer loop call of K number of digits 
    in each combination (indicates end of leaf)
https://leetcode.com/problems/subsets/
"""
class Solution:
    def subsets(self, nums):
        def dfs(res, idx = 0, curr=[]):
            if len(curr)==k:
                res.append(curr[:])            
                
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(res, i+1, curr)
                curr.pop()
            
            return res
        res = []
        for k in range(len(nums)+1):
            dfs(res)
        return res

def test(i, o):
    
    for item in o:
        if item not in Solution().subsets(i):
            print("Failure")
            return
        
    print("Success")
    
Input, Output = [1,2,3], [  [3], [1], [2], [1,2,3], [1,3],  [2,3], [1,2],[]]
test(Input, Output)
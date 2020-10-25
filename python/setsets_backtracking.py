"""
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
    if o == Solution().subsets(i): print("Success")
    else: print("Failure")

Input, Output = [1,2,3], [  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

test(Input, Output)
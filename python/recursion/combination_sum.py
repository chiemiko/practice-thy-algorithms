"""
Given an array of distinct integers candidates and a target integer target, return a list 
of all unique combinations of candidates where the chosen numbers sum to target. You may 
return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations
 are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.
"""


class Solution:
    def combinationSum(self, candidates, target):
        def dfs(i, curr_combo, res):
            if i >= len(candidates):
                return
            if sum(curr_combo) + candidates[i] > target:
                return
            elif sum(curr_combo) + candidates[i] == target:
                curr_combo.append(candidates[i])
                if curr_combo not in res:
                    res.append(curr_combo.copy())
                return
            else:
                curr_combo.append(candidates[i])
                # traverse remaining
                for next_i in range(i, len(candidates)):
                    dfs(next_i, curr_combo, res)
                curr_combo.pop()
                return

        res = []

        for i in range(len(candidates)):
            dfs(i, [], res)

        return res



candidates = [2,3,6,7]
target = 7
Output = [[2,2,3],[7]]
print(Solution().combinationSum(candidates, target) == Output)

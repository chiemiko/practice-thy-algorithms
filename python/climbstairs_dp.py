"""
MAIN IDEA:
    Save time and work by using dynamic programming,
    since there are only two ways to get to the final
    step -> countways(stepsn) = countways(stepsn-1) + countways(stepsn-2)

DP subproblem statement: 
    f(stepsleft) = f(stepsleft-1) + f(stepsleft-2)

ORIGINAL PROBLEM (leetcode 70):
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs_backtracking(self, n):
        """
        :type n: int
        :rtype: int
        """
        # method 1: backtracking
        def backtrack(nstepsleft):
            if nstepsleft == 0:
                return 1
            elif nstepsleft < 0:
                return 0
            return backtrack(nstepsleft-1) + backtrack(nstepsleft-2)
            
        numways =  backtrack(n)
        return numways

    def climbStairs_memo(self, n):
        # method 2: recursive memoization
        def backtrack(nstepsleft):
            if nstepsleft == 0:
                return 1
            elif nstepsleft < 0:
                return 0
            if not memo[nstepsleft]:
                memo[nstepsleft] = backtrack(nstepsleft-1) + backtrack(nstepsleft-2)
            return memo[nstepsleft]
            
        memo = [0]*(n+1)
        numways =  backtrack(n)
        return numways

    def climbStairs(self, n):
        # method 3: iterative tabulation
        tab = [0]*(n+1) 
        tab[1] = 1
        tab[2] = 2
        
        for i in range(3, n+1): 
            tab[i] = tab[i-1] + tab[i-2]
        return tab[n]

def test(input, output):
    if output == Solution().climbStairs(input): print("success")
    else: print("failure")

input, output = 2, 2
test(input, output)

input, output = 3, 3
test(input, output)

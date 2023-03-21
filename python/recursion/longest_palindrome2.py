class Solution:
    def solve(s):
        return


# s = "abaxyzzyx"
# output = "xyzzyx"
s = "abaxyzzyx"
"""
abaxyzzyx
     ^

MAIN IDEA is to iterate from the middle, since it's impossible to do 
a left/right two pointer system
"""

output = "bab"

print(Solution().solve(s) == output)
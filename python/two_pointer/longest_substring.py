"""

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 2
        res = 0
        while l<=r and r<len(s):
            print(l, r)
            if s[r] not in s[l:r]:
                r += 1
                res = max(res, len(s[l:r]))
            else:
                l = s[l:r].index(s[r])+1 + l

        return res if res > 0 else 1
    
s = "pwwkew"
output = 3
print(Solution().lengthOfLongestSubstring(s) == output)

# Input: s = "bbbbb"
# Output: 1

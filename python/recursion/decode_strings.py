"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

this solution errors aout -- recursive stack too large?! 
"""
class Solution:
    def encode(self, s):
        def dfs(curr= str, remaining=str , res=list):
            print('iterating')
            # used all s
            if len(remaining) == 0:
                print(f'what is the curr: {curr}')
                res.append(curr)
                print(res)
                return
            if len(curr.replace(' ', "")) == len(s):
                return

            # traverse
            curr_next1 = curr + ' ' + remaining[0]
            curr_next2 = curr + remaining[0]
            remaining = remaining[1:]

            if self.is_valid(curr_next1):
                dfs(curr_next1, remaining, res)
            if self.is_valid(curr_next2):
                dfs(curr_next2, remaining, res)
            return

        res = []
        dfs(curr="", remaining=s, res=res)
        return len(res)


    def is_valid(self, s):
        # validation rules - only numbers
        nums = s.split(' ')
        for num in nums:
            if num == "":
                return False
            if '0' in num[0]:
                return False
            if int(num) not in list(range(1, 27)):
                return False
        return True

s = "226"
Output = 3

print(Solution().encode(s)==Output)
# print(Solution().is_valid("2 2"))

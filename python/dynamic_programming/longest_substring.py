"""
Given a string s, find the length of the longest 
substring without repeating characters.

assumption: 
- substring means consecutive letters? 


can do either: 
option 1
    curr_substr = set()
    curr_length = 5

option 2
    curr_letters = []


abcabcbb
   ^

res = max(res, len(current_letters))
# kind of like dynamic programming

O(n) ? around?

TRICK: 
    when iterating and keeping LEFT index, make sure to add the left unused 
    potion as well
"""

def findSubstring():
    
    return

s = "abcabcbb"
expected= 3
print(findSubstring(s) == expected)
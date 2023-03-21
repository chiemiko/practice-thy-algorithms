"""
Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""

def isAnagram(s, t):
    """
    (slogs + tlogt) 
    """
    return sorted(s) == sorted(t)    

def findAnagrams(s, p):
    """ EASY! sliding window 
    o(n)*(slogs + tlogt) 
    """       
    
    return

s = "cbaebabacd"
p = "abc"
output = [0,6]

print(findAnagrams(s,p) == output)
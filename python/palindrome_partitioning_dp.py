class Solution(object):
    def partition(self, s: str) -> List[List[str]]:
        """
        131 - https://leetcode.com/problems/palindrome-partitioning/

        main idea: 
            tricky part is the isPalindrome(s[start:end]) substructure and understanding how to traverse the dfs... 
            to do this, use two pointer for inner string: if isPalindrome([s[current_idx:curr_end]]) == True -> add to current_list and DFS search the NEXT index as a starting point (end+1)
        
        Input: "aab"
        Output:
        [
          ["aa","b"],
          ["a","a","b"]
        ]
        
        brute force, use backtracking! 
        
        """
        # method 1: backtracking
        def valid_palindrome(s):
            if s==s[::-1]:
                print('palindrome: ' + s)
                return True
            else: return False
        
        def backtrack(curr_list=[],start=0):         
            print(f'current output:{output}')
            if start>=len(s):
                output.append(curr_list)
                print(f'finally got one: {curr_list}')
                print(output)
                print()

                return 
                
            # initiate backtrack for all other directions            
            for end in range(start, len(s)):
                print(f'start: {start}')
                print(f'end: {end}')
                # if valid palindrome is true -> add to the current list and then traverse NEXT CURR STRING RIGHT AFTER END INDEX ... end+1
                # if valid_palindrome(start, end):
                if valid_palindrome(s[start:end+1]):
                    curr_list.append(s[start:end+1])
                    backtrack(curr_list, end+1)
                    curr_list.pop()
            
            return           
            
#         def valid_palindrome(start, e):
#             """
#             takes in start and end idx of string
#             and returns True or False 

#             Approach - start from the outside in
            
#             0, 0
#             a
#             """
#             orig_s = start
#             orig_end = e
#             while start <= e:
#                 if s[start] != s[e]:
#                     return False
#                 start+=1
#                 e-=1
#             print(f"palindrome true: {s[orig_s: orig_end]}")
            
#             return True

        output = []
        backtrack()
        return output

def test(i, o):
    if o == Solution().dfs()

input, output = "aab", [["aa","b"],["a","a","b"]]
test(input, output)
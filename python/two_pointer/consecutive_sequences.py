"""

input 
[0 4 4 4 2 2 0 1]
count how many consecutive sequences there are


"""

class Solution:
    def solve(self, i):
        l, r = 0, 1
        ct = 0
        on_continuous = False
        while l<r and r<len(i):
            if i[l] == i[r]:
                on_continuous = True
                r += 1
            else:
                if on_continuous == True:
                    ct += 1
                    on_continuous = False

                l = r
                r+=1 
            
        return ct
    
# !! how can we keep track of the quick shifting? 
i = [0, 4, 4, 4, 2, 2, 0, 1]
output = 2
print(output == Solution().solve(i))
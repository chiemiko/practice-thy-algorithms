import heapq
from collections import Counter

class Solution():
    """    
    Main Ideas:
        - no need for PRIORITY QUEUE -> because do not 
            need to keep track of largest counts... 
    """
    def __init__(self):

        self.maxheap = []
        self.rescounts = 0

    def leastInterval(self, tasks, n):
        counts = Counter(tasks)        
        # initialize MAX heap -> (val, letter) 
        for key, val in counts.items():
            heapq.heappush(self.maxheap, (-val, key))
        
        while self.maxheap: # [(3, 'A'), (3, 'B')]
            countdown = 0
            temp = []
            if countdown<=n:
                self.rescounts+=1

                if self.maxheap:
                    freq, letter = heapq.heappop(self.maxheap)
                    freq +=1
                    if freq<0:
                        temp.append( (freq, letter) )
                    if not self.maxheap and not temp:
                        break

                countdown+=1

            for item in temp:
                heapq.heappush(self.maxheap, item )      
        print(self.rescounts)
        return 10

input = ("AAABBB", 3) # "AB--AB--AB" -> 10, "A--B--A--B--A--B" 16
output = 10

test = Solution().leastInterval(input[0], input[1])
if test == output: 
    print("success")
else:
    print("failure")
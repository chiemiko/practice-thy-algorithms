"""
Find kth largest element in an unsorted array of integers

input = [3, 2, 1, 5, 6, 4]
k = 2
"""
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = [-1*n for n in nums]
        heapq.heapify(heap)

        for i in range(k):
            res = heapq.heappop(heap)

        return -1*res

input = [3, 2, 1, 5, 6, 4]
k = 2
output = 5

print(Solution().findKthLargest(input, k) == output)

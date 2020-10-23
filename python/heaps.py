"""
Heaps practice

syntax: 
    https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

Kth largest element in an array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
import heapq

def heap_k_largest(nums, k):
    heap = []

    for item in nums:
        if len(heap) >= 4:
            if item > heap[0]:
                heapq.heappop(heap)
        heapq.heappush(heap, item) # min heap push when larger and larger maximums
    print(heap)


nums = [3,2,1,5,6,4, 10, 22, 112] 
k = 2
heap_k_largest(nums, k)
"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

for num in range(N, -1, -1) :
    print(num, end = " ")
"""
import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        meetings = sorted(intervals)
        print(meetings)

        min_heap = []
        for s,e in meetings:
            if s < min_heap[0]:
                heapq.heappush(min_heap, e)
            else:
                # just replace that earliest end time for meeting "room" with the latest
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, e)
        return len(min_heap)
        

intervals = [[0,30],[15,20],[5,10]]
Output= 2

print(Solution().minMeetingRooms(intervals) == Output)

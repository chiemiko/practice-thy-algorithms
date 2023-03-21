"""
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented 
by a 2D integer array tasks, where 
tasks[i] = [enqueueTimei, processingTimei] 
means that the i​​​​​​th​​​​ task will be available to process at 
enqueueTimei and will take processingTimei to finish 
processing.

You have a single-threaded CPU that can process at most 
one task at a time and will act in the following way:

PROCESS/LOGIC:
    if: 
        the CPU is idle and there are no available tasks to 
        process, the CPU remains idle.

    elif:
        If the CPU is idle and there are available tasks, 
            the CPU will choose the one with the shortest processing time. 

        If multiple tasks have the same shortest processing time, 
        it will choose the task with the smallest index.
        Once a task is started, the CPU will process the entire 
        task without stopping.

ORDER QUEUE BY: 
- cond1: available, cond2: shortest processing time
- cond3: earliest index

The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.



"""
class Solution:    
    """
    example [[7,10],[7,12],[7,5],[7,4],[7,2]]
    output = [4,3,2,0,1]
    
    RETURN INDICES


    """
    def get_order(self, t):
        res = []
        heap = []

        for time in range(0):
            
        return 

tasks = [[1, 2], [2, 4], [3, 2], [4,1]]
output = [0, 2, 3, 1]

print(Solution().get_order(tasks)==output)

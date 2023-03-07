class Solution:
    def twoSumLessThanK(self, nums):
        """
        which two numbers return maximum closest to 60

        [34, 23, 1, 24, 75, 33, 54, 8]

                            v     
        [1, 8, 23, 24, 33, 34, 54, 75]
                            ^

        k = 60

        1 + 75 = 76
        1 + 54 = 55
        8 + 54 = 64
        8 + 34 = 44
        23 + 34 = 57
        24 + 34 = 58

        33 + 34 - 77




        1 + 34 = 35



        if sum >= target:
            right -= 1
        
        else: 
            left += 1


        1.  set left and right indexes
        2. 
        
        """
        if not nums or len(nums) < 2:
            return -1
        
        nums = sorted(nums)
        if nums[0] >= k or nums[1] >= k:
            return -1
        l, r = 0, len(nums) - 1
        curr_res = nums[l] + nums[r]
        while l < r:
            sum = nums[l] + nums[r]
            print(l, r)
            print(f'sum: {sum}'
            )
            if sum > k:
                r -= 1
            elif sum == k:
                r -= 1
            else:
                curr_res = max(curr_res, sum) # USE MAX FOR SOME REASON
                l += 1
    
        return curr_res
        
# class Solution:
#     def twoSumLessThanK(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         answer = -1
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             sum = nums[left] + nums[right]
#             if (sum < k):
#                 answer = max(answer, sum)
#                 left += 1
#             else:
#                 right -= 1
#         return answer
    

input = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
k = 200
output = 198

print(Solution().twoSumLessThanK(input, k) == output)
"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int 
        :type nums: List[int] 
        :rtype: int
        """
        sum = head = 0
        res = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res, i - head + 1)
                sum -= nums[head]
                head += 1
        return res if res<=len(nums) else 0

s = Solution()
print(s.minSubArrayLen(3, (1,2,3,4,5)))

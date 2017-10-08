"""
53. Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thisSum = maxSum = nums[0]

        if len(nums) == 1:
            return maxSum
        
        # 每输入一个数据就进行即时处理
        for i in range(1,len(nums)):
            thisSum = max(thisSum + nums[i], nums[i])
            maxSum = max(thisSum, maxSum)
        return maxSum

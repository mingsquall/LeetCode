"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            # 直接找到非自身的目标数值，返回自身下标, 目标数值下标
            if target - nums[i] in nums and i != nums.index(target - nums[i]):
                return [i , nums.index(target - nums[i])]
        return []

class Solution1(object):
    def twoSum(self, nums, target):
        # hash建立{'数值':'下标'}的映射
        hash = {}
        # 循环nums数值, 判断并添加映射
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        # 无解
        return []

class Solution2(object):
    def twoSum(self, nums, target):
        hash = {}
        for index, num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num], index]
            hash[num] = index
        return []

s = Solution()
print(s.twoSum([0,1,5,2,9], 11))

s1 = Solution1()
print(s1.twoSum([0,1,5,2,9], 11))

s2 = Solution2()
print(s2.twoSum([0,1,5,2,9], 11))

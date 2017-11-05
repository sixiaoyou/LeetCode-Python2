'''
LeetCode 137:Single Number II
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Subscribe to see which companies asked this question.
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)==1:
            return nums[0]
        else:
            for i in range(len(nums)):
                if i==0 and nums[1]!=nums[0]:
                    return nums[0]
                elif i==len(nums)-1 and nums[-2]!=nums[-1]:
                    return nums[-1]
                else:
                    if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                        return nums[i]
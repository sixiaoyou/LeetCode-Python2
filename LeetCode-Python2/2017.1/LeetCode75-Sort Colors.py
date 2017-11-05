'''
LeetCode 75:Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a=nums.count(0)
        b=nums.count(1)
        for i in range(0,a):
            nums[i] = 0
        for j in range(a,a+b):
            nums[j] = 1
        for k in range(a+b, len(nums)):
            nums[k] = 2
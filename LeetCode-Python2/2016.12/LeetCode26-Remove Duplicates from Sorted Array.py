'''
LeetCode 26:Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question
'''
class SolutionV1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j + 1] = nums[j + 1], nums[i]
                j = j + 1
        return j + 1


#网友实现:http://blog.csdn.net/yyd19921214/article/details/47686983 (Python改写)
class SolutionV2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        else:
            j, k = 1, 1
            while (j < len(nums)):
                if nums[j] != nums[k - 1]:
                    nums[k] = nums[j]
                    k += 1
                j += 1
            return k





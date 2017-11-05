'''
LeetCode 80:Remove Duplicates from Sorted Array II
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

#网友实现：http://blog.csdn.net/tchenjx/article/details/54346384

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return len(nums)
        j,k=2,2
        while j<len(nums):
            if nums[j]!=nums[k-2]:
                nums[k]=nums[j]
                k+=1
            j+=1
        return k


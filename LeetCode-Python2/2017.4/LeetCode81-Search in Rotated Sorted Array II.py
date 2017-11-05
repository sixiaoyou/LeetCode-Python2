'''
LeetCode81:Search in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
'''



class SolutionV1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return nums.__contains__(target)


class SolutionV2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target not in nums:
            return False
        else:
            return True

class SolutionV3(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums=list(set(nums))
        for i in nums:
            if i==target:
                return True
        return False


class SolutionV4(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return True
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high -= 1
                else:
                    low += 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low += 1
                else:
                    high -= 1
        return False



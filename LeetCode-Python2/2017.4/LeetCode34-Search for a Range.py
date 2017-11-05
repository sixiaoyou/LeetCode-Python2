'''
LeetCode 34:Search for a Range
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        start = -1
        end = -1
        if nums == []:
            return [start, end]
        else:
            while low <= high:
                mid = (low + high) / 2
                flag1, flag2 = mid, mid
                if nums[mid] == target:
                    while nums[flag1] == target:
                        start = flag1
                        flag1 -= 1
                        if flag1 < 0:
                            break
                    while nums[flag2] == target:
                        end = flag2
                        flag2 += 1
                        if flag2 >= len(nums):
                            break
                    return [start, end]
                else:
                    if nums[mid] < target:
                        low += 1
                    elif nums[mid] > target:
                        high -= 1
        return [start, end]


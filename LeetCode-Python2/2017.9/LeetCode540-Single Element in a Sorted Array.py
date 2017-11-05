'''
LeetCode540. Single Element in a Sorted Array
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
'''
#【网友实现】:https://discuss.leetcode.com/topic/83310/short-compare-nums-i-with-nums-i-1
class SolutionV1(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


class SolutionV2(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        mark = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if mid % 2 == 0:
                if nums[mid] != nums[mid - 1]:
                    if nums[mid] != nums[mid + 1]:
                        return nums[mid]
                    else:
                        start = mid + 1
                else:
                    end = mid - 1

            else:
                if nums[mid] != nums[mid - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
        return nums[start]

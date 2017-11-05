'''
LeetCode 153:Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

#V1
class SolutionV1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)

#V2 网友实现:http://bookshadow.com/weblog/2014/10/16/leetcode-find-minimum-rotated-sorted-array/
class SolutionV2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low<high:
            mid=(low+high)/2
            if nums[mid]<=nums[high]:
                high=mid
            else:
                low=mid+1
        return nums[low]

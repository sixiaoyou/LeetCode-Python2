'''
LeetCode154:Find Minimum in Rotated Sorted Array II
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''

#网友实现:http://bookshadow.com/weblog/2014/11/06/find-minimum-in-rotated-sorted-array-ii/
class SolutionV1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left < right:
            mid =(left+right)/2
            if nums[mid]<nums[right]:
                right = mid
            elif nums[mid]>nums[right]:
                left = mid + 1
            else:
                return min(self.findMin(nums[:mid+1]),self.findMin(nums[mid+1:]))
        return nums[left]


class SolutionV2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)

class SolutionV3(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[0]
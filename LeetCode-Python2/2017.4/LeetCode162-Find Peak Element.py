'''
LeetCode 162:Find Peak Element
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

class SolutionV1(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return nums.index(max(nums))

#网友实现：http://bookshadow.com/weblog/2014/12/06/leetcode-find-peak-element/
class SolutionV2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        return self.search(nums, 0, size - 1)

    def search(self, nums, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return [start, end][nums[start] < nums[end]]
        mid = (start + end) / 2
        if nums[mid] < nums[mid - 1]:
            return self.search(nums, start, mid - 1)
        if nums[mid] < nums[mid + 1]:
            return self.search(nums, mid + 1, end)
        return mid

class SolutionV3(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        if len(nums)<3:
            return nums.index(max(nums))
        else:
            for i in range(1,len(nums)-1):
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                   a=i
            if nums[-1]>nums[-2]:
                a=len(nums)-1
            return a

# 极客学院版
class SolutionV4(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        start = 0
        end = n - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start


'''
LeetCode 303:Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''



class NumArrayV1(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0:
            i = 0
        if j >= len(self.nums):
            j = len(self.nums) - 1
        return sum(self.nums[i:j + 1])



#网友实现:http://bookshadow.com/weblog/2015/11/10/leetcode-range-sum-query-immutable/
class NumArrayV2(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        size = len(nums)
        self.sums = [0] * (size + 1)
        for x in range(size):
            self.sums[x + 1] += self.sums[x] + nums[x]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]




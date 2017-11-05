'''
LeetCode 268:Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''



#V1
class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=[]
        for i in range(len(nums)+1):
            nums1.append(i)
        return list(set(nums1).difference((set(nums))))[0]

#V2
class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[-1]!=len(nums):
            return len(nums)
        else:
            for i in range(len(nums)):
                if i!=nums[i]:
                    return i


#网友实现：http://bookshadow.com/weblog/2015/08/24/leetcode-missing-number/
#V3
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)


#V4
import operator

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = reduce(operator.xor, nums)
        b = reduce(operator.xor, range(len(nums) + 1))
        return a ^ b
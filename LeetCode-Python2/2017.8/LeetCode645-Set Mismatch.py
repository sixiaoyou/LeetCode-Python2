'''
/*

【Python3代码只要稍作更改，相除时通过math.floor来取整，故此Python2代码可做参考】
 【网友实现】: http://bookshadow.com/weblog/2017/07/24/leetcode-set-mismatch/
LeetCode645. Set Mismatch
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
 */
'''
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = len(nums)
        dmap = [0] * m
        for n in nums:
            if not dmap[n - 1]:
                dmap[n - 1] = 1
            else:
                return [n, (1 + m) * m / 2 + n - sum(nums)]
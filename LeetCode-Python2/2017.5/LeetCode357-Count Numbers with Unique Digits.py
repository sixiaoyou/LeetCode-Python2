#-*-coding:utf-8-*-
'''
【网友实现】:http://bookshadow.com/weblog/2016/06/13/leetcode-count-numbers-with-unique-digits/
LeetCode357:Count Numbers with Unique Digits
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.
'''


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [9]
        for x in range(9, 0, -1):
            nums += nums[-1] * x,
        # return sum(nums[:n]) + 1
        print nums
a=Solution()
a.countNumbersWithUniqueDigits(9)
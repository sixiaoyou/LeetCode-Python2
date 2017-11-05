'''
【Python3代码不变，故此Python2代码可做参考】
LeetCode633. Sum of Square Numbers
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
'''

import math

class Solution(object):
    def isInteger(self, c):
        temp = math.sqrt(c)
        if math.floor(temp) == temp:
            return True
        else:
            return False

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if self.isInteger(c):
            return True
        else:
            s = int(math.sqrt(c))
            for i in range(s, -1, -1):
                if self.isInteger(c - i * i):
                    return True
            return False
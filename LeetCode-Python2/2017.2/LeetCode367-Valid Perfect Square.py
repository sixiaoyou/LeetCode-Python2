'''
LeetCode367:Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
'''


class SolutionV1(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return int(num**0.5-1)*int(num**0.5+1)+1==num


class SolutionV2(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return str(num**0.5)[-1]=='0'
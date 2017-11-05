#-*-coding:utf-8 -*-


'''
LeetCode 172:Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''
import math
class SolutionV1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtyp
        """
        count = int(math.log(n, 5))
        sum = 0
        for i in range(1, count + 1):
            sum += n / (5 ** i)
        return sum


#网友实现:http://bookshadow.com/weblog/2014/12/30/leetcode-factorial-trailing-zeroes/
class SolutionV2(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=5
        sum=0
        while x<=n:
            sum+=n/x
            x*=5
        return sum

a=SolutionV2()
print a.trailingZeroes(1808548329)




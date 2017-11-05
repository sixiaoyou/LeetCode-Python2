'''
LeetCode 343:Integer Break
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
'''
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        product=1
        max1=0
        i=2
        if n==2:
            return 1
        else:
            while n / i >= 1:
                n1 = n % i
                if n1 != 0:
                    product1 = (n / i) ** i * n1
                    product2 = i ** (n / i) * n1
                    product3 = (n / i) ** (i - 1) * (n1 + n / i)
                    product = max(product1, product2, product3)
                else:
                    product = (n / i) ** i
                if product > max1:
                    max1 = product
                i += 1
            return max1

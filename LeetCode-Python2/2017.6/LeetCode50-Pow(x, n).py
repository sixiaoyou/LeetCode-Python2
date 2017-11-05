'''
【极客学院版】
LeetCode50. Pow(x, n)
Implement pow(x, n).
'''


class Solution(object):
    def pow(self, x, n):
        if n == 0:
            return 1
        else:
            half = self.pow(x, n >> 1)
            if n % 2 == 0:
                x = half * half
            else:
                x = half * half * x
        return x

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            if n > 0:
                return self.pow(x, n)
            else:
                return 1 / self.pow(x, -n)
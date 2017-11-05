'''
LeetCode 326. Power of Three
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #方法一：直接利用python的乘方运算
        ok=False
            for i in range(32):
                if n==3**i:
                    ok=True
            return ok

        #方法二：利用循环除
        x=1
        while x<=n:
            if x==n:
                return True
            x=x*3
        return False
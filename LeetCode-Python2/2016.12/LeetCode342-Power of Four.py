'''
LeetCode 342:Power of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #利用乘方运算
        ok = False
        if num > 0 and num < 2 ** 32 - 1:
            for i in range(32):
                if num == 4 ** i:
                    ok = True
        return ok

        #利用位运算
        if num>0 and num<2**32-1 and num&(num-1)==0 and (num-1)%3==0:
                    return True
                else:
                    return False
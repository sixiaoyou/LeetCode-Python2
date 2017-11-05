'''
【网友实现】:http://bookshadow.com/weblog/2016/07/13/leetcode-guess-number-higher-or-lower/
LeetCode374. Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
import random

class Solution(object):
    def guess(self,num,n):
        ra = random.randint(1,n)
        if num == ra:
            return 0
        elif num < ra:
            return 1
        else:
            return -1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while i <= n:
            mid = (i + n) / 2
            compare = self.guess(mid)
            if compare == 0:
                return mid
            elif compare == -1:
                n = mid - 1
            else:
                i = mid + 1

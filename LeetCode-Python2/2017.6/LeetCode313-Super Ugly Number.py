'''
【网友实现】:http://bookshadow.com/weblog/2015/12/03/leetcode-super-ugly-number/
LeetCode313. Super Ugly Number
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''


class Solution(object):
    def findMin(self, nums):
        return min(nums)

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        size = len(primes)
        q = [0] * n
        indexs = [0] * size
        values = [0] * size
        q[0] = 1
        for i in range(1, n):
            for j in range(size):
                values[j] = q[indexs[j]] * primes[j]
            q[i] = self.findMin(values)
            for k in range(len(values)):
                if values[k] == q[i]:
                    indexs[k] += 1
        return q[n - 1]
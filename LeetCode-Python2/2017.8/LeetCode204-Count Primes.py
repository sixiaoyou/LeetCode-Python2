'''
【网友实现】:http://bookshadow.com/weblog/2015/04/27/leetcode-count-primes/
LeetCode204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''



class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        iprime = [True] * max(n, 2)
        iprime[0], iprime[1] = False, False
        x = 2
        while x * x < n:
            if iprime[x * x]:
                p = x * x
                while p < n:
                    iprime[p] = False
                    p += x
            x += 1
        return sum(iprime)
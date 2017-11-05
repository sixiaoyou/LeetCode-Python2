'''
LeetCode397. Integer Replacement
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
'''


class Solution(object):
    # 网友实现
    def integerReplacement(self, n):

        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                if (n + 1) % 4 == 0 and n + 1 != 4:
                    n += 1
                else:
                    n -= 1
            count += 1
        return count

    # 【网友实现】:http://bookshadow.com/weblog/2016/09/11/leetcode-integer-replacement/
    def integerReplacementV2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n & 1 == 0: return self.integerReplacement(n / 2) + 1
        return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1

    def integerReplacementV3(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
                count += 1
            else:
                if n == 3:
                    count -= 1
                p, d = ((n + 1) / 2) % 2, ((n - 1) / 2) % 2
                if not p and d:
                    n += 1
                if p and not d:
                    n -= 1
                if not p and not d:
                    n -= 1

                count += 1
        return count

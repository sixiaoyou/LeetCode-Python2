'''
【极客学院版】
LeetCode264. Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
'''

import collections


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue2 = collections.deque()
        queue3 = collections.deque()
        queue5 = collections.deque()
        i, count = 1, 1
        while count < n:
            queue2.append(i * 2);
            queue3.append(i * 3);
            queue5.append(i * 5);
            min2, min3, min5 = queue2[0], queue3[0], queue5[0]
            minest = min(min(min2, min3), min5)
            if min2 == minest:
                queue2.popleft()
            if min3 == minest:
                queue3.popleft()
            if min5 == minest:
                queue5.popleft()
            i = minest
            count += 1
        return i


'''
网友实现:http://bookshadow.com/weblog/2017/03/26/leetcode-complex-number-multiplication/
LeetCode537:Complex Number Multiplication
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
'''

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        extract = lambda s: map(int, s[:-1].split("+"))
        m, n = extract(a)
        p, q = extract(b)
        return '%d+%di' % (m * p - n * q, m * q + n * p)


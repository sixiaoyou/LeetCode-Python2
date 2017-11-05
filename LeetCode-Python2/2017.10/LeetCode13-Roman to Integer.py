'''

LeetCode13. Roman to Integer
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
#网友实现
class SolutionV1(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        pre = 0
        for ch in s[::-1]:
            num = d[ch]
            if num >= pre:
                res += num
            else:
                res -= num
            pre = num
        return res

class SolutionV2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        res = ""
        start, ans, ls = 0, 0, len(s)
        while start < ls and s[start] == 'M':
            start += 1
            res += 'M'
        if len(res) != 0:
            ans += M.index(res) * 1000
            res = ""
        while start < ls and s[start] in ['C', 'D', 'M']:
            res += s[start]
            start += 1
        if len(res) != 0:
            ans += C.index(res) * 100
            res = ""
        while start < ls and s[start] in ['X', 'L', 'C']:
            res += s[start]
            start += 1

        if len(res) != 0:
            ans += X.index(res) * 10
        if start < ls:
            ans += I.index("".join(s[start:]))
        return ans

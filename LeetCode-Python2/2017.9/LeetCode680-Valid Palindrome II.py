'''
【Python3代码不变,故此Python2代码可做参考】
【网友实现】
LeetCode680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        res = s[::-1]
        if s == res:
            return True
        for i in xrange(length):
            if s[i] != s[length - i - 1]:
                return s[i + 1:length - i] == res[i:length - i - 1] or s[i:length - i - 1] == res[i + 1:length - i]
        return True

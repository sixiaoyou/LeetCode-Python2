'''
LeetCode 409:Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        count=0
        s1=collections.Counter(s)
        for i in s1:
                sum+=s1[i]
                if s1[i]%2!=0:
                    count+=1
                    sum-=1
        return sum+(count>0)




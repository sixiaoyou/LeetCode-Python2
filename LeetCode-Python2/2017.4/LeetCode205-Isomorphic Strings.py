'''
网友实现:http://bookshadow.com/weblog/2015/04/29/leetcode-isomorphic-strings/
LeetCode 205:Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
'''


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictS={}
        dictT={}
        for i in range(len(s)):
            if t[i] not in dictS and s[i] not in dictT:
                dictT[s[i]]=t[i]
                dictS[t[i]]=s[i]
            elif s[i]!=dictS[t[i]] or t[i]!=dictT[(s[i])]:
                return False
        return True

a=Solution()
print a.isIsomorphic("aa","ab")


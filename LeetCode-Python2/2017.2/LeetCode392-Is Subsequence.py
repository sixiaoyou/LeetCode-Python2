
#-*-coding:utf-8-*-
'''
LeetCode 392:Is Subsequence(网友实现)
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
'''

#V1(网友实现)
import collections

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        queue = collections.deque(s)
        for c in t:
            if not queue: return True
            if c==queue[0]:
                queue.popleft()
        return not queue


#V2
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=[]
        t1=list(t)
        index=-1
        ok=False
        for i in s:
            for j in range(len(t1)):
                if i not in t1:
                    return False
                else:
                    if i==t1[j]:
                         if j > index:
                            index=j
                            ok=True
                            break
                    else:
                        continue
            if not ok:
                return False
            ok=False
        return True

#V3(网友实现)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        if len(s)<0 or s==None:
            return True
        for i in range(len(s)):
            while index<len(t) and t[index]!=s[i]:
                index+=1
                print index,t[i],s[i]
            if index>= len(t):
                return False
            index+=1
        return True

'''
LeetCode 389:Find the Difference
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''

#V1
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(set(t)) == len(set(s)):
            if len(set(t)) == 1:
                return s[0]
            else:
                for i in s:
                    if s.count(i) != t.count(i):
                        return i
        else:
            return list(set(t).difference(set(s)))[0]


#V2
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        listS=list(s)
        listT=list(t)
        listS.sort()
        listT.sort()
        for i in range(len(listT)-1):
            if listT[i]!=listS[i]:
                return listT[i]
        return listT[-1]

#V3
import collections

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds = collections.Counter(s)
        dt = collections.Counter(t)
        return (dt - ds).keys().pop()

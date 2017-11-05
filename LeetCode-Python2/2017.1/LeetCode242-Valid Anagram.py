'''
LeetCode 242: Valid Anagram
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

#【极客学院版本】
class SolutionV1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None and t is None:
            return True
        elif s is not None and t is None:
            return False
        elif s is None and t is not None:
            return False
        else:
            if len(s) != len(t):
                return False
            n = len(s)
            arrayS = [0] * 26
            arrayT = [0] * 26
            for i in range(n):
                arrayS[ord(s[i]) - 97] += 1
                arrayT[ord(t[i]) - 97] += 1
            for j in range(26):
                if arrayS[j] != arrayT[j]:
                    return False
            return True


class SolutionV2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=s
        t1=t
        l=list(s1)
        m=list(t1)
        l.sort()
        m.sort()
        s1="".join(l)
        t1="".join(m)
        if s==t:
            return True
        elif len(s)==len(t)>1 and s!=t and s1==t1:
            return True
        else:
            return False

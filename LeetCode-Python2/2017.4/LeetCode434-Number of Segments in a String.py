'''
LeetCode 434:Number of Segments in a String
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''



#网友实现:https://discuss.leetcode.com/topic/70939/one-line-python-solution
class SolutionV1(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())



class SolutionV2(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if list(set(s.split(" ")))[0]=="" and len(set(s.split(" ")))==1:
            return 0
        else:
            return len(s.split(" "))-s.split(" ").count("")

#网友实现：https://discuss.leetcode.com/topic/70642/clean-java-solution-o-n
class SolutionV3(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in range(len(s)):
            if s[i]!=' ' and (i==0 or s[i-1]==' '):
                res+=1
        return res
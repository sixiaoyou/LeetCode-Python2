'''
LeetCode 58: Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''
import time

# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         list=[]
#         if len(s) != 0 and len(s)!=s.count(' '):
#             list=s.split(' ')
#             list.reverse()
#             for i in list:
#                 if i != '':
#                     return len(i)
#         else:
#             return 0

class SolutionV1(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list=[]
        if len(s) != 0:
            if len(set(s))==1 and '' in set(s):
                return 0
            else:
                list=s.split(' ')
                list.reverse()
                for i in list:
                    if i != '':
                        return len(i)
        else:
            return 0

class SolutionV2(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        flag=0
        for i in s[::-1]:
            if i!=' ':
                count+=1
                flag=1
            else:
                if flag:
                    break
        return count


if __name__ == '__main__':
    start=time.clock()
    hello=SolutionV1()
    print hello.lengthOfLastWord("Hello World")
    end=time.clock()
    print end-start
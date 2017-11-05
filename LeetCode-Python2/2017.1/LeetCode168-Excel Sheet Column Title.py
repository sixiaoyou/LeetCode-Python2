'''
LeetCode 168:Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dict = {}
        n1=1
        str = ''
        for i in range(len(string.uppercase) + 1):
            if i > 0:
                dict[i] = string.uppercase[i - 1]
        if n<=26:
            return dict[n]
        else:
            if n%26==0:
                while n/26>1:
                    n1=n%26
                    n=n/26
                    if n1==0:
                        str+='Z'
                str+=dict[n-1]
            else:
                while n/26>0:
                    n1=n%26
                    n=n/26
                    if n1==0:
                        str+='Z'
                    else:
                        str+=dict[n1]
                if n1!=0:
                    str+=dict[n]
            return str[::-1]
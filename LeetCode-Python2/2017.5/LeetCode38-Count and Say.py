'''
【极客学院版本】
LeetCode38:Count and Say
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return ""
        elif n==1:
            return "1"
        elif n==2:
            return "11"
        else:
            str1="11"
            sb=""
            for i in range(3,n+1):
                temp=str1[0]
                count=1
                for j in range(1,len(str1)):
                    if temp==str1[j]:
                        count+=1
                    else:
                        sb+=str(count)+str1[j]
                        count=1
                        temp=str1[j]
                sb+=str(count)+temp
                str1=sb
                sb=""
        return str1


'''
LeetCode504:Base 7
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''

class Solution(object):

    #【网友实现】:http://bookshadow.com/weblog/2017/02/12/leetcode-base-7/
    def convertToBase7V1(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = abs(num)
        ans = ''
        while n:
            ans += str(n % 7)
            n /= 7
        return ['', '-'][num < 0] + ans[::-1] or '0'

    def convertToBase7V2(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        a=abs(num)
        n=0
        str1=""
        while a/(7**n)!=0:
            n+=1
        n-=1
        while a!=0:
            if a/(7**n)!=0 and n>0:
                str1 += str(a/(7**n))
                a=a-(a/(7**n))*(7**n)
            elif n==0:
                str1+=str((a/(7**n))*(7**n))
                a = a - (a / (7 ** n)) * (7 ** n)
            else:
                str1+="0"
            n-=1
        while num%7==0 :
                num=num/7
                str1+="0"
        if num<0:
            str1="-"+str1
        return str1


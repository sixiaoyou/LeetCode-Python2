'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
#V1:网友实现:http://bookshadow.com/weblog/2016/10/09/leetcode-add-strings/
class Solution1(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        carry = 0
        idx1, idx2 = len(num1), len(num2)
        while idx1 or idx2 or carry:
            digit = carry
            if idx1:
                idx1 -= 1
                digit += int(num1[idx1])
            if idx2:
                idx2 -= 1
                digit += int(num2[idx2])
            carry = digit > 9
            result.append(str(digit % 10))
        return ''.join(result[::-1])


#V2
class Solution2(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum1=0
        sum2=0
        for i in range(len(num1)):
                sum1+=int(num1[i])*(10**(len(num1)-i-1))
        for j in range(len(num2)):
                sum2+=int(num2[j])*(10**(len(num2)-j-1))
        return str(sum1+sum2)




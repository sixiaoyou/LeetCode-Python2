'''
LeetCode 67:Add Binary
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class SolutionV1(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c=int(a,2)+int(b,2)
        return str(bin(c)[2:])



#网友实现:https://discuss.leetcode.com/topic/13698/short-ac-solution-in-java-with-explanation
class SolutionV2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sb=""
        i,j,carry=len(a)-1,len(b)-1,0
        while i>=0 or j>=0:
            sum=carry
            if i>= 0:
                sum+=int(a[i])
                i-=1
            if j>=0:
                sum+=int(b[j])
                j-=1
            sb+=str(sum%2)
            carry=sum/2
        if carry!=0:sb+=str(carry)
        return sb[::-1]






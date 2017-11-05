'''
LeetCode 9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
注意点：121,12321是回文的格式
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list=[]
        sum=0
        z=0
        b=x=121
        if  x>=0 and x<=2**31-1:
            while True:
                y=b%10
                b=b/10
                z+=1
                list.append(y)
                if b==0:
                    break
            for j in list:
                if z > 0:
                    sum += j * 10 ** (z - 1)
                    z= z - 1
            if sum==x:
                return True
            else:
                return False
        else:
            return False
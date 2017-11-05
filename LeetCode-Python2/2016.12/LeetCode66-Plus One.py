'''
LeetCode 66:Plus One
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        list1=list[::-1]
        list2=[]
        sum=0
        for i in range(len(list1)):
            sum+=list1[i]*10**i

        sum1=sum+1
        while True:
            y = sum1 % 10
            sum1 = sum1 / 10
            list2.append(y)
            if sum1 == 0:
                break
        list3=list2[::-1]
        return list3

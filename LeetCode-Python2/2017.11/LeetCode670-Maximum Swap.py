'''
LeetCode.670. Maximum Swap
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]

'''
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        list1,list2,list3,mark,mark2,temp,temp1=[],[],[],-1,True,0,0
        ls=list(str(num))
        list1=list(map(int,str(num)))
        list3 = sorted(list1, reverse=True)
        for j in range(len(list3)):
            if mark2 and list3[j]>list1[j]:
                ls[j]=str(list3[j])
                temp=list3[j]
                temp1=str(list1[j])
                mark2=False
            if list1[j] == temp:
                mark = j
        if mark>0:
            ls[mark]=temp1
        list2=map(str,ls)
        return int("".join(list2))
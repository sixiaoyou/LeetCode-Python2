'''
【Python3代码不变，故可参照此Python2代码】
LeetCode859. Buddy Strings
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
'''
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        if A == B:
            if len(A)==len(set(A)):
                return False
            return True
        ls = []
        for i in range(len(A)):
            if A[i]!=B[i]:
                ls.append(A[i])
                ls.append(B[i])
        if len(ls)!=4:
            return False
        if ls[0]!=ls[3] or ls[1]!=ls[2]:
            return False
        return True
'''
【Python3代码不变，故可参照此Python2代码】
LeetCode821. Shortest Distance to a Character
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        list = []
        for i in range(len(S)):
            if S[i] == C:
                list.append(0)
            else:
                start, end, count1, count2 = i, i, 0, 0

                while start > 0 and S[start] != C:
                    start -= 1
                    count1 += 1
                while end < len(S) - 1 and S[end] != C:
                    end += 1
                    count2 += 1
                if S[start] != C and S[end] == C:
                    list.append(count2)
                elif S[end] != C and S[start] == C:
                    list.append(count1)
                else:
                    list.append(min(count1, count2))
        return list

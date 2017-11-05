'''
LeetCode541. Reverse String II
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
'''
import math

#【网友实现】:http://bookshadow.com/weblog/2017/03/12/leetcode-reverse-string-ii/
class SolutionV1(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ''
        round = int(math.ceil(len(s) / (2.0 * k)))
        for x in range(round):
            ans += s[x * 2 * k : (x * 2 + 1) * k][::-1]
            ans += s[(x * 2 + 1) * k : (x * 2 + 2) * k]
        return ans

class SolutionV2(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        size = len(s)
        listS = list(s)
        if k == 1:
            return s
        if size<k:
            return  "".join(listS[::-1])
        if size >=k and size<2*k:
            return "".join(s[:k][::-1])+s[k:]
        else:
            start = 0
            end = 2*k-1
            while end<=size:
                listS[start:start+k]=listS[start:start+k][::-1]
                ans = size - end -1
                if ans < k:
                    listS[end+1:] = listS[end+1:][::-1]
                    return "".join(listS)
                elif ans>=k and ans<2*k:
                    listS[end+1:end+k+1] = listS[end+1:end+k+1][::-1]
                    return "".join(listS)
                start+=2*k
                end+=2*k
            return "".join(listS)
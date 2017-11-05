'''
【Python3代码不变，故此Python2代码可做参考】
LeetCode647. Palindromic Substrings
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''
import collections


class SolutionV1(object):
    def isPalindromicString(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        length = len(s)
        for i in range(length):
            start = 0
            end = i
            while end != length:
                if self.isPalindromicString(s[start:end + 1]):
                    count += 1
                start+= 1
                end+= 1
        return count

#【网友实现】:http://bookshadow.com/weblog/2017/07/24/leetcode-palindromic-substrings/
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        queue = collections.deque((x, x) for x in range(size))
        for i in range(size - 1):
            if s[i] == s[i + 1]:
                queue.append((i, i + 1))
        ans = 0
        while queue:
            x, y = queue.popleft()
            ans += 1
            if x - 1 >= 0 and y + 1 < size and s[x - 1] == s[y + 1]:
                queue.append((x - 1, y + 1))
        return ans
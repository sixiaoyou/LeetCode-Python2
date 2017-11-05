'''
LeetCode 3:Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


#网友实现:http://bookshadow.com/weblog/2015/04/05/leetcode-longest-substring-without-repeating-characters/
class SolutionV1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, start, end = 0, 0, 0
        countDict = {}
        for c in s:
            end += 1
            countDict[c] = countDict.get(c, 0) + 1
            while countDict[c] > 1:
                countDict[s[start]] -= 1
                start += 1
            ans = max(ans, end - start)
        return ans


#网友实现:https://discuss.leetcode.com/topic/11632/a-python-solution-85ms-o-n
class SolutionV2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=maxLength=0
        dict={}
        for i in range(len(s)):
            if s[i] in dict and start<=dict[s[i]]:
                start=dict[s[i]]+1
            else:
                maxLength=max(maxLength,i-start+1)
            dict[s[i]]=i
        return maxLength


'''
LeetCode 387:First Unique Character in a String
Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #方法一：利用字典来统计每个字符出现的字数
        letters = {}
        for i in s:
            letters[i]=letters[i]+1 if i in letters else 1
        for i in xrange(len(s)):
            if letters[s[i]] == 1:
                print i
        print -1

        #方法二：利用数组来统计每个字符出现的次数
        letters=[0] * 26
        for i in s:
            letters[ord(i)-97]+=1
        for i in xrange(len(s)):
            if letters[ord(s[i])-97]==1:
                print i

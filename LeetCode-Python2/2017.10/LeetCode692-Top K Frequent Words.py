'''
【Python3代码不变，故可以参照此Python2代码】
LeetCode692. Top K Frequent Words
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
Can you solve it in O(n) time with only O(k) extra space?
'''
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dict = {}
        for i in words:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]+=1
        li = sorted(dict.items(),key = lambda item:-item[1])
        res = []
        start,end = 0,0
        while start < len(li):
            while end < len(li) and li[end][1]==li[start][1]:
                end+=1
            li=li[:start]+sorted(li[start:end])+li[end:]
            start = end
        for j in range(k):
            res.append(li[j][0])
        return res
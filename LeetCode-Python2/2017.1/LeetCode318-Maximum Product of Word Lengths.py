'''
网友实现：http://bookshadow.com/weblog/2015/12/16/leetcode-maximum-product-word-lengths/
LeetCode 318:Maximum Product of Word Lengths
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''
import collections
import string
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        es = [set() for x in range(26)]
        ml = collections.defaultdict(int)
        for w in words:
            num = sum(1 << (ord(x) - ord('a')) for x in set(w))
            ml[num] = max(ml[num], len(w))
            for x in set(string.lowercase) - set(w):
                es[ord(x) - ord('a')].add(num)
        ans = 0
        for w in words:
            r = [es[ord(x) - ord('a')] for x in w]
            if not r: continue
            r = set.intersection(*r)
            for x in r:
                ans = max(ans, len(w) * ml[x])
        return ans
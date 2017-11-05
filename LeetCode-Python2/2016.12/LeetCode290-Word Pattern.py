'''
LeetCode 290:Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype:
        """
        str = str.split(' ')
        dict = {}
        dict1 = {}
        list = []
        if len(str) != len(pattern):
            return False
        if len(set(str)) != len(set(pattern)):
            return False
        for i in xrange(len(str)):
            if pattern[i] not in list:
                list.append(pattern[i])
                dict[pattern[i]] = str[i]
                dict1[str[i]] = pattern[i]
            else:
                if str[i] != dict[pattern[i]]:
                    return False
                if pattern[i] != dict1[str[i]]:
                    return False

        return True
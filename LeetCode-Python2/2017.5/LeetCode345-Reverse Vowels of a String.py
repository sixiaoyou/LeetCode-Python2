'''
LeetCode345:Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''


import re

#【网友实现】:http://bookshadow.com/weblog/2016/04/23/leetcode-reverse-vowels-string/
class SolutionV1(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

class SolutionV2(object):
    list = []
    check = "aeiouAEIOU"

    def replace1(self, r1):
        for j in r1:
            if j in self.check:
                self.list.append(j)
                r1 = r1.replace(j, "^", 1)
        return r1

    def replace2(self, r2):
        for j in r2:
            if j == "^":
                r2 = r2.replace(j, self.list.pop(), 1)
        return r2

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringS = s.split(" ")
        return " ".join(map(self.replace2, map(self.replace1, stringS)))



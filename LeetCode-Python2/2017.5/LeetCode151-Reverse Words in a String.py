'''
LeetCode151:Reverse Words in a String
Total Accepted: 152546
Total Submissions: 970904
Difficulty: Medium
Contributor: LeetCode
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''
class Solution(object):
    #【网友实现】:http://bookshadow.com/weblog/2014/10/16/leetcode-reverse-words-string/
    def reverseWordsV1(self, s):
        """
          :type s: str
          :rtype: str
          """
        words = s.split()
        words.reverse()
        return " ".join(words)


    def reverseWordsV2(self, s):
        """
        :type s: str
        :rtype: str
        """
        list=[]
        if  len(s.strip(' '))==0:
             return ""
        list=s.strip(' ').split(" ")[::-1]
        while '' in list:
            list.remove('')
        return ' '.join(list)


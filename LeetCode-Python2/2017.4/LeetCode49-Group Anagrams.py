'''
LeetCode-49:Group Anagrams
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict={}
        list1=[]
        b=''
        for i in strs:
            a=list(i)
            a.sort()
            for j in a:
                b+=j
            if b not in dict:
                dict[b]=[i]
            else:
                dict[b].append(i)
            b=''
        for j in dict:
            list1.append(dict[j])
        return list1

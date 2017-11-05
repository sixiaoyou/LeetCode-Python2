'''
LeetCode 524. Longest Word in Dictionary through Deleting
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
'''

import collections
from operator import itemgetter, attrgetter
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isFormed(j):
            ok = True
            queue = collections.deque(j)
            for i in s:
                if queue:
                    if i == queue[0]:
                        queue.popleft()
            if queue:
                ok = False
            return ok
        res = []
        dict={}
        dict2={}
        for j in d:
              if isFormed(j):
                  res.append(j)
        if res==[]:
            return ""
        else:
            for i in res:
                dict[i]=len(i)
            dict1 = sorted(dict.iteritems(), key=lambda k:k[1],reverse=True)
            list=[]
            for i in dict1:
                list.append(i[0])
            return min(x for x in list if len(x)==len(list[0]))
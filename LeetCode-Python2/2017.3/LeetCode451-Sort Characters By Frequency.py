'''
LeetCode 451: Sort Characters By Frequency
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

#V1
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype
        """
        s1=""
        dict={}
        list1=[]
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        list1=sorted(dict.iteritems(),key=lambda d:d[1],reverse=True)
        for i in list1:
            s1+=i[0]*i[1]
        return s1

#V2


import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(c*t for c, t in collections.Counter(s).most_common())
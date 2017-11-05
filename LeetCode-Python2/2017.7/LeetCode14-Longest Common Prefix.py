'''
LeetCode14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
'''

#【网友实现】https://discuss.leetcode.com/topic/27913/sorted-the-array-java-solution-2-ms
class SolutionV1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        if strs == []:
            return ""
        start = strs[0]
        end = strs[-1]
        s = ""
        ls, le = len(start), len(end)
        for i in range(ls):
            if le > i and start[i] == end[i]:
                s += start[i]
            else:
                return s
        return s


class SolutionV2(object):
    def isCommonPrefix(self, setStrs, str, end):
        for i in setStrs[1:]:
            if str[:end] != i[:end]:
                return False
        return True

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        setStrs = sorted(set(strs), key=len)
        end = len(setStrs[0])
        while end > 0:
            if self.isCommonPrefix(setStrs, setStrs[0], end):
                return setStrs[0][:end]
            end -= 1
        return ""
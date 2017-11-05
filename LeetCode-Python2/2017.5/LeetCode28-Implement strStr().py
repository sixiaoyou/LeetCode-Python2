'''
LeetCode28:Implement strStr()
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class SolutionV1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except:
            return -1


#【极客学院版】实现细节清晰,非考察Api的调用，但TLE。
class SolutionV2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        for i in range(m):
            count = 0
            j = 0
            while j < n and i + j < m:
                if haystack[i + j] != needle[j]:
                    break
                else:
                    count += 1
                j += 1
            if count == n:
                return i
        return -1


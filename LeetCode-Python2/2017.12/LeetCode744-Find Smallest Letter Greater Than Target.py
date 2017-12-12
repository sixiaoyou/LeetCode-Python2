'''
【Python3代码不变，故可参照此Python2代码】
LeetCode744. Find Smallest Letter Greater Than Target
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.

'''
class SolutionV1:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in range(len(letters)):
                if letters[i] > target:
                    return letters[i]
                elif i == len(letters) - 1 :
                    return letters[0]

#【网友实现】https://discuss.leetcode.com/topic/113450/easy-binary-search-in-java-o-log-n-time
class SolutionV2(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        length = len(letters)
        if target >= letters[length - 1]:
            return letters[0]
        else:
            target = chr(ord(target) + 1)
        start, end = 0, length - 1
        while (start < end):
            mid = start + (end - start) / 2
            if letters[mid] == target:
                return letters[mid]
            elif letters[mid] < target:
                start = mid + 1
            else:
                end = mid
        return letters[end]



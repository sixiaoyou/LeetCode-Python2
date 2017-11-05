'''
LeetCode594. Longest Harmonious Subsequence
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
'''
import collections

#[网友实现]:http://bookshadow.com/weblog/2017/05/21/leetcode-longest-harmonious-subsequence/
class SolutionV1(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        ans = 0
        lastKey = lastVal = None
        for key, val in sorted(cnt.items()):
            if lastKey is not None and lastKey + 1 == key:
                ans = max(ans, val + lastVal)
            lastKey, lastVal = key, val
        return ans

class SolutionV2(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        list = []
        max1 = 0
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]+=1
        for j in dict:
            list.append(j)
        if len(list) <= 1:
            return 0
        else:
            list.sort()
            for i in range(len(list)-1):
                if list[i+1] - list[i] == 1:
                    max1 = max(max1 , dict[list[i+1]]+dict[list[i]])
            return max1
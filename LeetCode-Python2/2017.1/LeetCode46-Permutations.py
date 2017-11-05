'''
网友实现：http://bookshadow.com/weblog/2016/09/09/leetcode-permutations/
LeetCode 46:Permutations
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: return [nums]
        ans=[]
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for y in self.permute(n):
                ans.append([num] + y)
        return ans
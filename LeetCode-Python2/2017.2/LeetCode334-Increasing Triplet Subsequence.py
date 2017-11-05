
'''
网友实现：http://bookshadow.com/weblog/2016/02/16/leetcode-increasing-triplet-subsequence/
LeetCode 334. Increasing Triplet Subsequence
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=b=None
        for n in nums:
            if a is None or a >= n:
                a=n
            elif b is None or b >= n:
                b=n
            else:
                return True
        return False


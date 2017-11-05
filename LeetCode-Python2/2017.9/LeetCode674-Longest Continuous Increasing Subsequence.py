'''
【Python3代码不变,故此Python2代码可做参考】
LeetCode674. Longest Continuous Increasing Subsequence
Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
'''
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        temp = 0
        length = len(nums)
        if length < 2:
            return length
        else:
            for i in range(length-1):
                if nums[i+1]>nums[i]:
                    count+=1
                else:
                    if temp < count:
                        temp = count
                    count = 1
            if temp < count:
                temp = count
            return temp

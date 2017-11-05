'''
【Python3代码不变，故此Python2代码可做参考】
LeetCode643. Maximum Average Subarray I
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length = len(nums)
        list = [0,0]
        start,sum1= 0,0
        end = k
        while end <= length:
                if start!=0:
                    sum1+=nums[end-1]-nums[start-1]
                    if sum1>list[0]:
                        list[0] = sum1
                        list[1] = start
                start+=1
                end+=1
        return sum(nums[list[1]:list[1]+k])/float(k)
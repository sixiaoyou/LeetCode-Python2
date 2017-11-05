'''
LeetCode697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        dict2 = {}
        dict3 = {}
        ln = len(nums)
        mark = False
        for i in range(ln):

            if nums[i] not in dict1:
                dict1[nums[i]] = 1
                dict2[nums[i]] = i
                dict3[nums[i]] = i
            else:
                mark = True
                dict1[nums[i]] += 1
                dict2[nums[i]] = i - dict3[nums[i]] + 1
        list = sorted(dict1.items(), key=lambda k: -k[1])
        max1 = list[0][1]

        max2 = dict2[list[0][0]]
        for i in range(len(list)):
            if list[i][1] == max1:
                if dict2[list[i][0]] < max2:
                    max2 = dict2[list[i][0]]
            else:
                break
        return max2 if mark else max2 + 1
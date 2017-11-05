'''
【Python3代码不变，故此Python2代码可做参考】
LeetCode611. Valid Triangle Number
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
'''

#【网友实现】:http://bookshadow.com/weblog/2017/06/11/leetcode-valid-triangle-number/
#双指针
class SolutionV1(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        count =0
        nums.sort()
        for i in range(length-2):
            if nums[i]==0:
                continue
            k = i+2
            for j in range(i+1,length-1):
                while k<length and nums[i]+nums[j]>nums[k]:
                    k+=1
                count+=k-j-1
        return count

#O(n2)+二分
class SolutionV2(object):
    def binarySearch(self, nums, start, target):
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        length = len(nums)
        nums.sort()
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                k = self.binarySearch(nums, j + 1, nums[i] + nums[j])
                count += k - j - 1
        return count

#TLE解 Java下AC 三重循环
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        count = 0
        nums.sort()
        for i in range(length-2):
            for j in range(i+1,length-1):
                for k in range(j+1,length):
                    if nums[i]+nums[j]>nums[k]:
                        count+=1
        return count
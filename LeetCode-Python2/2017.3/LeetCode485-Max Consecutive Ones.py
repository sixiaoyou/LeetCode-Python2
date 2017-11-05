'''
LeetCode 485:Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Subscribe to see which companies asked this question.
'''

#v1
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(0)==0:
            return len(nums)
        elif nums.count(1)==0:
            return 0
        else:
            previous=nums.index(0)
            behind=0
            lenNums=[]
            for i in xrange(len(nums)):
                if i>0 and nums[i]==1 and nums[i-1]==0 and (i-1)!=previous:
                      previous=i-1
                if i < len(nums) - 1 and nums[i] == 1 and nums[i + 1] == 0:
                          behind = i + 1
                          lenNums.append(behind - previous-1)
                else:
                     continue
            lenNums.append(nums.index(0) - 0)
            lenNums.append(len(nums) - behind - 1)
            return lenNums

#V2
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(0)==0:
                    return len(nums)
                else:
                    previous=nums.index(0)
                    lenNums=[]
                    for i in xrange(len(nums)):
                        if nums[i]==0 and i!=nums.index(0):
                            lenNums.append(i-previous-1)
                            previous=i
                    lenNums.append(nums.index(0)-0)
                    lenNums.append(len(nums)-previous-1)
                    return max(lenNums)
#V3
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength=count=0
        for i in nums:
            if i==1:
                count+=1
                maxLength=max(maxLength,count)
            else:
                count=0
        return maxLength
'''
LeetCode 53:Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
class SolutionV1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[-1]
        maxNum=sum
        for i in range(len(nums)-2,-1,-1):
            sum=max(nums[i],sum+nums[i])
            maxNum=max(sum,maxNum)
        return maxNum



#网友实现:http://www.cnblogs.com/boring09/p/4252780.htmls
class SolutionV2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum=max(nums)
        thisNum=0
        for i in nums:
            thisNum+=i
            if thisNum>maxNum:
                maxNum=thisNum
            elif thisNum<0:
                thisNum=0
        return maxNum


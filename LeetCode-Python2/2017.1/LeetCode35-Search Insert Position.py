'''
LeetCode 35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class SolutionV1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
                 return 0
        else:
            if target in nums:
                return nums.index(target)
            for i in range(len(nums)-1):
                # if nums[i]==target:
                #     return i
                if nums[i]<target and nums[i+1]>target:
                    return i+1
            if target==nums[-1]:
                return len(nums)-1
            else:
                return len(nums)


#网友实现：http://www.cnblogs.com/ccsccs/articles/4215628.html
class SolutionV2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l+=1
            else:
                r-=1
        return l


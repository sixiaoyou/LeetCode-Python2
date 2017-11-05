'''
网友实现：http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/
LeetCode 287:Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''


class SolutionV1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0

        # Keep advancing 'slow' by one step and 'fast' by two steps until they
        # meet inside the loop.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Start up another pointer from the end of the array and march it forward
        # until it hits the pointer inside the array.
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]

            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow


class SolutionV2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)>>1
            cnt=sum(x<=mid for x in nums)
            if cnt>mid:
                high=mid-1
            else:
                low=mid+1
        return low


class SolutionV3(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=i
            else:
                return i

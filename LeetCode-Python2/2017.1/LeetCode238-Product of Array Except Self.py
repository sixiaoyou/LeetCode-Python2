'''
LeetCode 238. Product of Array Except Self
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = []
        nums1 = []
        total = reduce(lambda x, y: x * y, nums)

        if nums.count(0) > 1:
            return [0] * len(nums)
        else:
            if nums.count(0) == 1:
                nums2 = copy.deepcopy(nums)
                nums2.remove(0)
                total1 = reduce(lambda x, y: x * y, nums2)
                for i in nums:
                    if i != 0:
                        nums1.append(total / i)
                    else:
                        nums1.append(total1)
            else:
                for i in nums:
                    nums1.append(total / i)
        return nums1

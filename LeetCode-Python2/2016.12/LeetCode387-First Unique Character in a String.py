'''
LeetCode 349：Intersection of Two Arrays
Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = []
        for i in nums2:
            if i in nums1:
                nums3.append(i)
        return nums3